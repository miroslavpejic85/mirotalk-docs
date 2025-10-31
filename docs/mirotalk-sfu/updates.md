# Updates (self-hosted)

When you update to the newest version of MiroTalk SFU using the `./sfuUpdate.sh` script, any customized files (such as your branding in public/views) get overwritten. This happens because the update process replaces the entire base code and can’t automatically preserve client-specific modifications.

So after each update, you’ll need to reapply your own branding files unless they’re separated from the tracked source code and also if there are changes in the `.env - config.js` file need to update it as well accordingly.

Here are a few recommended options to handle this more smoothly:

## ✅ Option 1: Use `git stash` before updating

If your changes are small (like branding or a few layout edits), you can use:

```bash
cd mirotalksfu
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

* `Small edits`: use git stash.
* `Ongoing customizations`: use a custom-branding branch.
* `Docker deployment`: mount your branding as volumes.

This will make future updates much smoother and prevent your branding from being overwritten.