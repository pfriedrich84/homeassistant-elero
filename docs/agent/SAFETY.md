# Agent Safety

Tool-neutral safety guidance for coding agents working on `homeassistant-elero`.

## Allowed by default

- Read, search, and make targeted edits to repository files.
- Run validation commands listed in [`CHECKS.md`](CHECKS.md).
- Use read-only Git commands for orientation: `git status`, `git diff`, `git log`, `git branch`.
- Add or update documentation when it improves maintainability and keeps links valid.
- Add tests or lightweight validation scripts that do not require secrets or hardware.

## Ask first / avoid unless explicitly requested

- Destructive filesystem operations, especially recursive deletes.
- History rewriting or destructive Git operations such as force-push, hard reset, or rebase of shared branches.
- Broad formatting or large refactors unrelated to the task.
- Adding new runtime dependencies or changing Home Assistant/HACS metadata in ways that affect installation.
- Changing release tags, GitHub Actions, or publishing behavior.
- Assuming a final Home Assistant `radio_frequency` API shape where the code currently has TODO placeholders.

## Never do

- Do not print, copy, or modify secrets from Home Assistant config directories, `.env` files, tokens, or runtime data.
- Do not add ESP32 firmware, CC1101 SPI drivers, interrupt-driven sniffing loops, or timing-critical RF code to this repository.
- Do not hard-code LilyGO/CC1101 as the only supported backend.
- Do not weaken Home Assistant security, config-entry safety, review gates, or validation without an explicit security-driven task.

## Before finishing

Run the relevant checks from [`CHECKS.md`](CHECKS.md), or state clearly why a check was not run.
