# Migrate a Team to Another OCS Instance

This guide walks through moving a team — its chatbots, configuration, and chat history — from one Open Chat Studio (OCS) instance to another. A common case is moving a team off the hosted `openchatstudio.com` onto a self-hosted instance, but the same process works between any two OCS servers.

This is operator-level work: you'll run Django management commands on a server you administer. It assumes shell access to the target server and Team Admin access on the source server.

## Source and target servers

- **Source server** — the OCS instance you are migrating the team *from*.
- **Target server** — the self-hosted instance you are migrating the team *to*.

All commands in this guide run **on the target server**, and pull data from the source over HTTPS.

## How it works

Migration runs as a single management command, `sync_team`, on the target server. It authenticates to the source, pulls the team's data over HTTPS, and recreates it locally.

The command creates a small SQLite tracking database (named after the team slug) on the target server. This tracks what has already been imported and how record IDs map between the two servers, which is what makes the command safe to run more than once — each rerun resumes where the last one left off and pulls in anything new, such as chats that happened in the meantime.

Sensitive fields, such as provider credentials, are never sent in plain text: the source encrypts ("seals") them to a public key you register beforehand, and the sync command decrypts them on the target using the matching private key.

## What is not migrated

These need to be re-established on the target server after migration:

- API keys
- OAuth applications — clients must re-authenticate against the target server
- Slack installations
- Open (unaccepted) team invitations

!!! note "Team members come across"
    Existing (accepted) team members are migrated along with the team, including their roles. The
    sync links each member to an account with the same username if one already exists on the target,
    and creates the account otherwise — newly created users are emailed a password-reset link so they
    can set a password. Only *pending* invitations (above) are left behind, so re-invite those people
    on the target.

## Prerequisites

- Team Admin access to the team on the source server.
- The ability to run `manage.py` commands on the target server.
- Access to upload files to the target server's storage backend (for example, an S3-compatible bucket) — you'll move the team's files across in [step 2](#2-export-your-teams-files-source-server).
- A way to generate an RSA key pair — for example OpenSSL, Python with the `cryptography` package, or an online RSA key generator.

## 1. Set up the target server

Stand up and configure the self-hosted OCS instance you're migrating to, if you haven't already. See the [local development setup](https://developers.openchatstudio.com/getting-started/local-setup/) or [Docker setup](https://developers.openchatstudio.com/getting-started/docker-setup/) guides, or the [OCS GitHub repository](https://github.com/dimagi/open-chat-studio) for deployment options.

!!! warning "Source and target must match versions"
    The sync command checks that the source and target are on the same schema/migration state before syncing anything, and aborts if they don't match. Make sure the target server is running the latest OCS version before you continue.

## 2. Export your team's files (source server)

A team's files live in a storage backend (such as an S3-compatible bucket), so you move them across separately:

1. On the source server, go to **Team Settings** and open the **Data** section, headed **Data & migration**. This section is only visible to Team Admins.
2. In the **Download team files** card, select **Download** to export all of the team's files as a zip. See [Download Team Files](../how-to/download_team_files.md) for what the export contains and how long it stays available.
3. Unzip the archive and upload its contents to the target server's storage backend (for example, an S3-compatible bucket).

!!! note "Preserve the folder layout"
    Upload the files using the same folder layout and storage keys as in the zip. The file records that `sync_team` creates on the target point at those exact storage keys — if the layout doesn't match, the target won't be able to find the files.

## 3. Generate an encryption key pair and register the public key

Secrets such as provider credentials are encrypted in transit. The source seals them to a public key you register in the **Migration public key** card; only the holder of the matching private key — the target server — can unseal them.

Generate an RSA key pair with OpenSSL:

```bash
openssl genrsa -out privkey.pem 2048
openssl rsa -in privkey.pem -pubout -out pubkey.pem
```

Or, using Python's `cryptography` library:

```python
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

with open("privkey.pem", "wb") as f:
    f.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    ))

with open("pubkey.pem", "wb") as f:
    f.write(private_key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    ))
```

!!! tip "No OpenSSL or Python?"
    Any tool that produces a standard RSA-2048 PEM key pair works, including an in-browser generator such as [cryptotools.net/rsagen](https://cryptotools.net/rsagen). Prefer one that generates the keys locally in your browser so the private key never leaves your machine.

Then:

1. On the source server, paste the public key (`pubkey.pem`) into the **Public Key** field of the **Migration public key** card, in the same **Data** section under Team Settings, and select **Save key**.
2. Copy the **private key** (`privkey.pem`) to the target server. You'll pass its path to `sync_team` in [step 6](#6-run-the-sync-command-target-server).

!!! warning "Keep the private key safe"
    Anyone with the private key can decrypt the secrets sealed for your team. Store it outside of version control and restrict access to it on the target server.

## 4. Create an API key (source server)

Create an API key for your user on the source server — the sync command uses it to authenticate. The user the key belongs to must be a Team Admin of the team you're migrating. The key only needs **read** permissions, since the sync command only reads data from the source. See [API Access](api_access.md) for how to generate an API key from your profile page.

## 5. Enable migration mode (source server)

In the **Data** section on the source server, turn on the **Migration mode** checkbox in the **Migration public key** card and select **Save key**. This step is required. If migration mode isn't enabled, `sync_team` stops with the error: "Migration mode needs to be enabled on the source team before you can continue."

!!! warning "Effects of migration mode"
    While migration mode is enabled on the source:

    - Scheduled messages, event triggers, timeout triggers, and scheduled triggers all stop firing.
    - Live chat traffic is unaffected and continues to work normally.
    - A banner appears on every page of the team: "This team is undergoing a migration. Do not create or edit chatbots until the migration is complete."

## 6. Run the sync command (target server)

Run `sync_team` on the target server, pointing it at the source:

```bash
python manage.py sync_team \
  --source-url "https://www.openchatstudio.com" \
  --api-key "<your-api-key>" \
  --team-slug "<team-slug>" \
  --private-key-path "/path/to/privkey.pem" \
  --state-dir "/path/to/state-dir"
```

The arguments are:

- `--source-url` — the base URL of the source server.
- `--api-key` — the API key you created on the source server ([step 4](#4-create-an-api-key-source-server)).
- `--team-slug` — the slug of the team you're migrating.
- `--private-key-path` — the path to the private key you copied to the target server ([step 3](#3-generate-an-encryption-key-pair-and-register-the-public-key)). Alternatively, set the `SYNC_TEAM_PRIVATE_KEY` environment variable to the private key's PEM contents instead of passing a path. This is often easier in a containerized environment, where you can inject it as a secret rather than mounting a key file. If both are provided, `--private-key-path` takes precedence.
- `--state-dir` — the directory where the checkpoint SQLite database is stored. Point every rerun at the same directory so the command can resume from where it left off.
- `--follow` (optional) — keep the command running after the first pass and pull new rows from the source on a repeating interval. See [Keep the sync running with --follow](#keep-the-sync-running-with-follow).
- `--interval` (optional) — the number of seconds to wait between passes when you use `--follow`. The default is 10.

Where you run this depends on how you run OCS:

- **From source**, run it in the project directory with your virtual environment activated.
- **In Docker**, run it inside the web container, adjusting the service name as needed:

```bash
docker compose exec web python manage.py sync_team \
  --source-url "https://www.openchatstudio.com" \
  --api-key "<your-api-key>" \
  --team-slug "<team-slug>" \
  --private-key-path "/path/to/privkey.pem" \
  --state-dir "/path/to/state-dir"
```

The command creates a SQLite tracking database named after the team slug in the `--state-dir` directory. It's safe to run `sync_team` again at any point — each run picks up only what's changed since the last run, so you can use it to pull in a delta later (see [step 8](#8-verify-and-do-a-final-sync)), or run it continuously with `--follow`.

!!! warning "Persist the state directory in containerized environments"
    In a containerized environment, the state directory won't survive container restarts or redeployments unless you persist it. Either bind mount `--state-dir` to a durable location on the host, or manually copy it out and back in if you plan to restart or redeploy the container before running the command again. If the state directory is lost, the next run starts from scratch instead of resuming.

### Keep the sync running with --follow

By default, `sync_team` makes one pass over the source and exits.
With `--follow`, it keeps running, so you can leave it running through the channel cutover in [step 7](#7-re-register-channel-webhooks-target-server) instead of doing a separate final run afterwards.

```bash
python manage.py sync_team \
  --source-url "https://www.openchatstudio.com" \
  --api-key "<your-api-key>" \
  --team-slug "<team-slug>" \
  --private-key-path "/path/to/privkey.pem" \
  --state-dir "/path/to/state-dir" \
  --follow
```

After each pass, the command prints a line in this form, then waits `--interval` seconds and starts the next pass from its stored cursors:

```text
pass N: X rows synced, last new row T ago
```

To stop the command:

- Press **Ctrl+C** (or send `SIGTERM`) once to stop after the current page finishes.
- Press **Ctrl+C** a second time to abort immediately.

When the command stops, it prints a report.
The report includes the number of rows synced per model, plus the number of rows adopted and the number of rows kept because the target was edited (see [How the sync handles existing and changed data](#how-the-sync-handles-existing-and-changed-data)).

### How the sync handles existing and changed data

Each pass reads every resource page by page from its stored cursor and stores the cursor after each page commits.
The sync applies these rules:

- **Unchanged rows are skipped.** A row with the same source `updated_at` as at the last sync is not written again.
- **Existing participants are adopted.** If a participant or participant data row has not been imported yet, and the target already has one with the same unique key, the sync maps the source row onto the target row. The target row is left unchanged.
- **Target edits are kept.** If a session, chat, participant, or participant data row on the target has an `updated_at` later than the last revision the sync wrote, the sync leaves the row unchanged.
- **Rows created during the sync are caught up.** If a row's parent has no translation yet, the sync re-reads the parent's resource and retries the row. This lets the sync keep up with a source that is still receiving traffic. If the parent is still missing, for example because it was deleted or is outside the chatbot selection, the sync fails with `UnresolvedForeignKey`.
- **Rate limits are retried.** If the source returns a `429` response, the sync waits for the `Retry-After` period and retries. If the header is missing, it uses its normal backoff.

!!! note "Known limitation"
    A nullable foreign key that points to a parent created during the same run is set to null. It is not caught up.

## 7. Re-register channel webhooks (target server)

Once the team's data has synced, channel webhooks still point at the source server. Re-point them by running:

```bash
python manage.py reregister_webhooks --team-slug "<team-slug>"
```

To avoid losing messages that arrive during the switch, start `sync_team` with `--follow` before you run this command, and leave it running in another shell.
See [Keep the sync running with --follow](#keep-the-sync-running-with-follow).

Whether a channel updates automatically depends on its **messaging provider**, not just the platform:

- **Telegram** channels always update automatically.
- **WhatsApp** and **Facebook Messenger** channels update automatically when they are served through **Twilio**.

!!! note "This step is the cutover"
    Re-registering webhooks is the point where live traffic moves from the source to the target. Until you run it, incoming messages keep flowing to the source; afterwards they flow to the target. Individual channels may see a brief gap while the messaging provider propagates the new webhook URL.

The command prints a report of which channels it re-registered and which it couldn't. These need their webhooks re-registered by hand:

- **WhatsApp or Messenger via the Meta Cloud API** — reconfigure or recreate the channel on the target server.
- **WhatsApp via Turn.io** — update the webhook URL in the Turn.io console.
- **SureAdhere** — reconfigure the channel on the target server.

A few channel types aren't handled by this command at all and must be repointed separately:

- **Slack** — Slack apps are configured at the workspace level, not per channel; reinstall or reconnect the app against the target server.
- **Web widget embeds** — re-embed the [chat widget](../chat_widget/index.md) pointing at the target server.
- **API clients** — point them at the target server's base URL.

## 8. Verify and do a final sync

Test each channel against the target server and confirm chatbots respond as expected.

If `sync_team --follow` is running:

1. After all webhooks point at the target, watch the pass output.
2. When the passes report no new rows for a few minutes, the remaining data has been copied.
3. Press **Ctrl+C** to stop the command.

If you did not use `--follow`, run `sync_team` one more time to pull in any messages or updates that arrived on the source while you were switching channels over.

## After the migration

Migration mode is a per-server setting, and the source and target need **opposite** settings once the target takes over as the live server:

| Server | Migration mode | Why |
|---|---|---|
| Source | Keep **enabled** | Stops the source from sending the team's scheduled messages and events, now that the target is live and doing that instead. |
| Target | **Disable** | Lets the target start sending the team's scheduled messages and events as the new live server. `sync_team` enabled it automatically when it created the team ([step 6](#6-run-the-sync-command-target-server)) so the target wouldn't double-send while the source was still live — turn it off once cutover is complete. |

## Troubleshooting

**Sync aborts with a schema/version mismatch error**
: The source and target are running different OCS versions or migration states. Upgrade (or downgrade) the target so its migration state matches the source, then retry.

**Sync fails because secrets can't be unsealed**
: The source has sealed secret fields for the team, but `sync_team` wasn't given a matching private key. Pass `--private-key-path` pointing at the private key from [step 3](#3-generate-an-encryption-key-pair-and-register-the-public-key).

**Sync fails with `UnresolvedForeignKey`**
: A row refers to a parent that the sync cannot find on the source, usually because the parent was deleted or is outside the chatbot selection. The sync re-reads the parent's data before it fails, so a parent created on the source during the run does not cause this error.

**Sync pauses with rate-limit (429) responses**
: The sync waits for the source's `Retry-After` period and retries automatically. No action is needed.

**Data edited on the target is not overwritten by the sync**
: This is expected. The sync keeps target edits to sessions, chats, participants, and participant data. The report lists how many rows were kept for each model.

**Files are missing or broken on the target**
: The synced file records point at storage keys from the source. Confirm the files were uploaded to the target's storage backend under the exact same keys as in the exported zip (see [step 2](#2-export-your-teams-files-source-server)).

## See also

- [Team Settings](../concepts/team/index.md)
- [API Access](api_access.md)
- [Chat Widget](../chat_widget/index.md)
