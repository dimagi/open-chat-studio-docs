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

1. On the source server, go to **Team Settings** and open the **Data Export** section. This section is only visible to Team Admins.
2. Download all of the team's files as a zip.
3. Unzip the archive and upload its contents to the target server's storage backend (for example, an S3-compatible bucket).

!!! note "Preserve the folder layout"
    Upload the files using the same folder layout and storage keys as in the zip. The file records that `sync_team` creates on the target point at those exact storage keys — if the layout doesn't match, the target won't be able to find the files.

## 3. Generate an encryption key pair and register the public key

Secrets such as provider credentials are encrypted in transit. The source seals them to a public key you register; only the holder of the matching private key — the target server — can unseal them.

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

1. On the source server, register the **public key** (`pubkey.pem`) in the same **Data Export** section under Team Settings.
2. Copy the **private key** (`privkey.pem`) to the target server. You'll pass its path to `sync_team` in [step 6](#6-run-the-sync-command-target-server).

!!! warning "Keep the private key safe"
    Anyone with the private key can decrypt the secrets sealed for your team. Store it outside of version control and restrict access to it on the target server.

## 4. Create an API key (source server)

Create an API key for your user on the source server — the sync command uses it to authenticate. The user the key belongs to must be a Team Admin of the team you're migrating. The key only needs **read** permissions, since the sync command only reads data from the source. See [API Access](api_access.md) for how to generate an API key from your profile page.

## 5. Enable migration mode (source server)

In the **Data Export** section on the source server, enable migration mode for the team. The sync endpoints refuse to serve a team that isn't in migration mode, so this step is required.

!!! warning "Effects of migration mode"
    While migration mode is enabled on the source:

    - The source stops sending the team's scheduled messages.
    - Live chat traffic is unaffected and continues to work normally.

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

The command creates a SQLite tracking database named after the team slug in the `--state-dir` directory. It's safe to run `sync_team` again at any point — each run picks up only what's changed since the last run, so you can use it to pull in a delta later (see [step 8](#8-verify-and-do-a-final-sync)).

!!! warning "Persist the state directory in containerized environments"
    In a containerized environment, the state directory won't survive container restarts or redeployments unless you persist it. Either bind mount `--state-dir` to a durable location on the host, or manually copy it out and back in if you plan to restart or redeploy the container before running the command again. If the state directory is lost, the next run starts from scratch instead of resuming.

## 7. Re-register channel webhooks (target server)

Once the team's data has synced, channel webhooks still point at the source server. Re-point them by running:

```bash
python manage.py reregister_webhooks --team-slug "<team-slug>"
```

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

Test each channel against the target server and confirm chatbots respond as expected. Once you've confirmed everything is working, run `sync_team` one more time to pull in any messages or updates that arrived on the source while you were switching channels over.

## After the migration

!!! warning "Don't disable migration mode on the source"
    Once migration is complete, leave migration mode **enabled** on the source server. Disabling it makes the source start sending the team's scheduled messages again, which will conflict with the now-live target server. Keep it enabled until the team is deleted from the source server. A Team Admin can delete the team from **Team Settings** on the source once you're confident the migration is complete and the target is serving all traffic.

## Troubleshooting

**Sync aborts with a schema/version mismatch error**
: The source and target are running different OCS versions or migration states. Upgrade (or downgrade) the target so its migration state matches the source, then retry.

**Sync fails because secrets can't be unsealed**
: The source has sealed secret fields for the team, but `sync_team` wasn't given a matching private key. Pass `--private-key-path` pointing at the private key from [step 3](#3-generate-an-encryption-key-pair-and-register-the-public-key).

**Files are missing or broken on the target**
: The synced file records point at storage keys from the source. Confirm the files were uploaded to the target's storage backend under the exact same keys as in the exported zip (see [step 2](#2-export-your-teams-files-source-server)).

## Related content

- [Team Settings](../concepts/team/index.md)
- [API Access](api_access.md)
- [Chat Widget](../chat_widget/index.md)
