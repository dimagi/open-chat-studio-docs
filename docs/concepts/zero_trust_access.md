# Zero Trust Access for Self-Hosted Deployments

This page explains how to expose a self-hosted Open Chat Studio instance to your team without opening ports on your server or configuring a public IP address. It is written for server administrators and DevOps engineers.

## What is Zero Trust tunneling?

Zero Trust tunneling lets you publish an internal service to the internet through an outbound-only encrypted connection. Your server initiates the connection to a cloud edge; no inbound firewall rules are required. Access is then gated by identity, every user must authenticate before the application responds, regardless of where they are connecting from.

The practical result is that your team can reach `ocs.your-org` from any network, but only after they prove who they are.

## When to use this approach

Use Zero Trust tunneling when:

- You are running Open Chat Studio on a server without a static public IP or domain.
- You want to avoid exposing the application port directly to the internet.
- You need fine-grained access control based on email addresses, identity providers, or device posture.
- You want audit logs of every access attempt.

## Supported providers

Open Chat Studio has been tested with the following Zero Trust tunnel providers. The concepts are the same across providers; only the tooling differs.

| Provider | Guide |
|---|---|
| Cloudflare Tunnel (cloudflared) | [Cloudflare Tunnel setup guide](../how-to/cloudflare_tunnel.md) |

Other providers, such as Tailscale Funnel, ngrok, or AWS Verified Access, follow the same conceptual model and can be configured using the provider's own documentation.

## How it works (conceptual)

1. You install a lightweight connector daemon on the server running Open Chat Studio.
2. The daemon opens an outbound connection to the provider's edge network.
3. The provider creates a public hostname (e.g., `ocs.your-org`) that routes through that connection.
4. Users access the hostname from their browser. The provider's edge enforces an identity check before forwarding the request.
5. Optionally, users install a WARP or VPN client on their device to satisfy device-posture requirements.

No tunnel configuration details, CIDR ranges, or port mappings need to be shared with end users.

## Cloudflare Tunnel

Cloudflare Tunnel (`cloudflared`) is a free, production-ready option that integrates with Cloudflare Zero Trust (formerly Cloudflare Access). It requires a domain managed in Cloudflare DNS.

See the full setup guide: [Cloudflare Tunnel setup guide](../how-to/cloudflare_tunnel.md).

Once the tunnel is running, share the end-user connection guide with your team members:
[Zero Trust Administration](../how-to/zero_trust_admin.md)
