# Cloudflare Tunnel Setup

This guide walks a server administrator through publishing a self-hosted Open Chat Studio instance using Cloudflare Tunnel (`cloudflared`) and Cloudflare Zero Trust. Completing it requires a Cloudflare account with a domain managed in Cloudflare DNS.

!!! note "Prerequisite"
    Read the [Zero Trust Access overview](../concepts/zero_trust_access.md) before starting this guide.

## Prerequisites

- A Cloudflare account (free tier is sufficient for most deployments).
- A domain or subdomain managed in Cloudflare DNS (e.g., `your-org.com`).
- Open Chat Studio running locally and reachable at `http://localhost:8000` (or similar).
- `cloudflared` CLI installed on the same server. [Download cloudflared](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/downloads/).

## Step 1: Authenticate cloudflared

```bash
cloudflared tunnel login
```

A browser window opens. Select the zone (domain) you want to use. `cloudflared` writes a certificate to `~/.cloudflared/cert.pem`.

## Step 2: Create a named tunnel

```bash
cloudflared tunnel create ocs-tunnel
```

Note the tunnel UUID printed in the output, you will need it in the next step.

## Step 3: Configure the tunnel

Create `~/.cloudflared/config.yml`:

```yaml
tunnel: <YOUR_TUNNEL_UUID>
credentials-file: /root/.cloudflared/<YOUR_TUNNEL_UUID>.json

ingress:
  - hostname: ocs.your-org.com
    service: http://localhost:8000
  - service: http_status:404
```

Replace `ocs.your-org.com` with the hostname you want to use and `localhost:8000` with the address of your Open Chat Studio instance.

## Step 4: Create a DNS record

```bash
cloudflared tunnel route dns ocs-tunnel ocs.your-org.com
```

This creates a `CNAME` record in Cloudflare DNS pointing `ocs.your-org.com` to the tunnel.

## Step 5: Run the tunnel

For a quick test:

```bash
cloudflared tunnel run ocs-tunnel
```

For production, install `cloudflared` as a system service:

```bash
cloudflared service install
systemctl start cloudflared
systemctl enable cloudflared
```

## Step 6: Configure Cloudflare Access (identity gate)

1. In the [Cloudflare Zero Trust dashboard](https://one.dash.cloudflare.com/), go to **Access > Applications**.
2. Click **Add an application** and select **Self-hosted**.
3. Set the **Application domain** to `ocs.your-org.com`.
4. Under **Policies**, create a policy that allows access by email domain or specific email addresses.
5. Save the application.

Anyone who reaches `ocs.your-org.com` will now be prompted to authenticate through Cloudflare Access before the application responds.

## WARP device access

If you want to enforce device-posture checks, ensuring only enrolled corporate devices can connect, enable the WARP client requirement in your Access policy.

### Enrol a device

1. Ask the team member to install the WARP client and join your Zero Trust organisation. Share the end-user guide with them:
   **[WARP: User Access Guide](./zero_trust_admin.md)**
2. In the Zero Trust dashboard, go to **Settings > WARP Client** and configure the enrolment permissions (email domain or specific emails).
3. Optionally, add a **Device Posture** rule under **Settings > WARP Client > Device posture** to gate access on serial number, OS version, or certificate presence.

## Revoking access

To remove a user's access:

- For email-based policies: remove their email from the Access policy.
- For WARP-enrolled devices: revoke the device under **My Team > Devices** in the Zero Trust dashboard.

## Useful references

- [Cloudflare Tunnel documentation](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/)
- [Cloudflare Access documentation](https://developers.cloudflare.com/cloudflare-one/policies/access/)
- [WARP client download](https://developers.cloudflare.com/cloudflare-one/connections/connect-devices/warp/download-warp/)
- End-user guide: [WARP: User Access Guide](./zero_trust_admin.md)
