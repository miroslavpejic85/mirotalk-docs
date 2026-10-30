# Updates (self-hosted)

## ✅ Recommended: rebrand via `.env` and use the default update script

Configure branding and UI options in `.env` with [HTML injection](rebranding.md) (`BRAND_HTML_INJECTION=true`) and keep the frontend files untouched. Your local `.env` and `config.js` are not tracked by Git, so the default update script does not overwrite these files.

### Migrating existing branding

The P2P configuration update makes UI settings environment-driven. If you previously customized the `brand` object in `app/src/config.js`, move those values to the matching variables in `.env` (for example, `brand.htmlInjection` → `BRAND_HTML_INJECTION`, `brand.app.language` → `UI_LANGUAGE`, and `brand.app.translationMode` → `UI_TRANSLATION_MODE`). Review the new [environment template](https://github.com/miroslavpejic85/mirotalk/blob/master/.env.template) for the full list.

Update your local `config.js` from the latest [`config.template.js`](https://github.com/miroslavpejic85/mirotalk/blob/master/app/src/config.template.js), merging any other local application changes rather than overwriting them blindly. The current template maps the branding environment variables into the `brand` configuration.

For `Docker`:

```bash
#!/bin/bash

cd mirotalk
git pull
docker-compose down
docker-compose pull
docker image prune -f
docker-compose up -d
```

For `PM2`:

```bash
#!/bin/bash

cd mirotalk
git pull
sudo npm ci
pm2 restart app/src/server.js
```

Save it as `p2pUpdate.sh`, make it executable with `chmod +x p2pUpdate.sh`, and run `./p2pUpdate.sh` (see the [Self-Hosting Guide](self-hosting.md) for the full setup).

After each update, compare your `.env` and `config.js` with the latest [`.env.template`](https://github.com/miroslavpejic85/mirotalk/blob/master/.env.template) and [`config.template.js`](https://github.com/miroslavpejic85/mirotalk/blob/master/app/src/config.template.js) and add any new variables.

## Customized frontend files

If you edit the frontend files directly (`BRAND_HTML_INJECTION=false`, files in `public/views`), the update replaces the base code and overwrites those edits. In that case, preserve your edits with one of these options:

## ✅ Option 1: Use `git stash` before updating

If your changes are small (like branding or a few layout edits), you can use:

```bash
cd mirotalk
git stash push -m "My branding changes"
git pull
docker-compose down
docker-compose pull
docker image prune -f
docker-compose up -d
git stash pop
```

This saves your local edits, updates the base code, and then reapplies your customizations.
If any merge conflicts appear, you can resolve them manually.

## ✅ Option 2: Create a dedicated `“custom-branding” branch`

For more extensive or ongoing custom work, it’s better to create a branch:

```bash
git checkout -b custom-branding
```

Commit all your modifications there.
When a new version is released:

```bash
git checkout main
git pull origin main
git checkout custom-branding
git merge main
```

This lets you merge updates from the main repo into your custom branch while keeping your branding intact.

## ✅ Option 3: Mount your branding via `Docker volumes`

If you’re deploying with Docker Compose, you can keep your branding outside the repo and mount it into the container:

```yaml
volumes:
  - ./custom/views:/app/public/views
```
This way, updates won’t touch your custom files, they’ll stay completely separate from the update process.

In short:

* `Rebranding via .env`: use the default update script, nothing to reapply.
* `Small edits`: use git stash.
* `Ongoing customizations`: use a custom-branding branch.
* `Docker deployment`: mount your branding as volumes.

This will make future updates much smoother and prevent your branding from being overwritten.