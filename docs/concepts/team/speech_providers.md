# Speech Service Providers

Speech service providers enable voice capabilities in Open Chat Studio, including text-to-speech (TTS) and speech-to-text (STT). Configuring a speech provider allows chatbots to synthesize spoken audio from text and transcribe audio input to text.

## Supported providers

- **ElevenLabs** — TTS, STT, and voice management including custom voice cloning

## ElevenLabs

[ElevenLabs](https://elevenlabs.io) is an AI audio platform offering high-quality voice synthesis and transcription.

### Capabilities

| Capability | Details |
|---|---|
| Text-to-Speech (TTS) | Converts text to MP3 audio using ElevenLabs voices |
| Speech-to-Text (STT) | Transcribes audio using ElevenLabs Scribe v2 |
| Voice sync | Syncs available voices from the ElevenLabs catalog to OCS |

### Setup

1. Obtain an API key from your [ElevenLabs account](https://elevenlabs.io).
2. In Open Chat Studio, navigate to **Team Settings → Speech Service Providers**.
3. Add a new provider, select **ElevenLabs**, and enter your API key.
4. On creation, OCS will automatically sync available voices from your ElevenLabs catalog.

### Voices

When you create or edit an ElevenLabs provider, OCS fetches and stores the voices available in your ElevenLabs account. You can trigger a manual re-sync from the provider's edit page to pick up newly added voices.

**Custom voices:** Custom voices must be created directly in ElevenLabs. OCS does not support creating custom voices. Once created in ElevenLabs, they will be synced to OCS the next time a sync runs (automatically on provider creation, or manually on request).

OCS does not support creating custom voices directly — manage your voice library in ElevenLabs and let OCS sync the results.
