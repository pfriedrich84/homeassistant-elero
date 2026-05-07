# GitHub Setup

## Create Repository

Create a new public GitHub repository:

```text
pfriedrich84/homeassistant-elero
```

Recommended settings:

- Public
- Issues enabled
- Description: Home Assistant custom integration for Elero RF devices
- Topics:
  - home-assistant
  - hacs
  - elero
  - rf
  - radio-frequency
  - cover
  - smarthome

## Push Initial Files

From the extracted starter ZIP:

```bash
git init
git add .
git commit -m "Initial HACS custom integration skeleton"
git branch -M main
git remote add origin git@github.com:pfriedrich84/homeassistant-elero.git
git push -u origin main
```

## First Release

Once the skeleton validates:

```bash
git tag v0.0.1
git push origin v0.0.1
```

Then create a GitHub Release for `v0.0.1`.

## HACS Custom Repository Test

In Home Assistant:

1. Open HACS.
2. Open Custom repositories.
3. Add `https://github.com/pfriedrich84/homeassistant-elero`.
4. Category: Integration.
5. Install.
6. Restart Home Assistant.
