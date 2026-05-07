# HACS Notes

HACS expects a custom integration repository to contain exactly one integration below:

```text
custom_components/<domain>/
```

For this project:

```text
custom_components/elero/
```

Required files include:

```text
custom_components/elero/__init__.py
custom_components/elero/manifest.json
README.md
hacs.json
```

## Custom Repository Installation

During development, this repository can be added to HACS as a custom repository:

1. HACS → three-dot menu → Custom repositories.
2. Add the GitHub repository URL.
3. Select category: Integration.
4. Download the integration.
5. Restart Home Assistant.
6. Add Elero from Settings → Devices & services.

## Default HACS Repository

Later, after the project is stable, it may be submitted as a default HACS repository.

Expected requirements:

- public GitHub repository
- valid HACS repository layout
- HACS validation action
- Hassfest validation action
- GitHub release
- issues enabled
- repository description and topics
- brand assets if required
- stable README
