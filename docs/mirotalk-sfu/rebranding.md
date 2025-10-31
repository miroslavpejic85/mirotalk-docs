# Rebranding



!!! warning "License Required"

Rebranding requires at least a 👉 **[Regular License](https://codecanyon.net/item/mirotalk-sfu-webrtc-realtime-video-conferences/40769970)**, available on CodeCanyon.

---

There are two ways to rebrand MiroTalk SFU:

1. **From `.env` file** with `BRAND_HTML_INJECTION` enabled (recommended)

---

## Landing Page

```bash
APP_TITLE="<h1>MiroTalk SFU</h1> Free browser based Real-time video calls.<br />Simple, Secure, Fast."
APP_DESCRIPTION="Start your next video call with a single click. No download, plug-in, or login is required."
JOIN_DESCRIPTION="Pick a room name.<br />How about this one?"
JOIN_BUTTON_LABEL="JOIN ROOM"
JOIN_LAST_LABEL="Your recent room:"
```

![sfu-landing](../images/sfu/landing.png)

You can also hide optional landing page sections:

```bash
SHOW_TOP_SPONSORS=false
SHOW_FEATURES=false
SHOW_TEAMS=false
SHOW_TRY_EASIER=false
SHOW_POWERED_BY=false
SHOW_SPONSORS=false
SHOW_ADVERTISERS=false
SHOW_FOOTER=false
```

---

## New Room Page

![sfu-new](../images/sfu/newroom.png)

```bash
NEW_ROOM_TITLE="Pick name. <br />Share URL. <br />Start conference."
NEW_ROOM_DESC="Each room has its disposable URL. Just pick a name and share."
```

---

## Who Are You Page

![sfu-way](../images/sfu/whoareyou.png)

```bash
WHO_ARE_YOU_TITLE="Who are you?"
WHO_ARE_YOU_DESCRIPTION="If you're the presenter, please log in now.<br />Otherwise, kindly wait for the presenter to join."
WHO_ARE_YOU_BUTTON_LOGIN_LABEL="LOGIN"
WHO_ARE_YOU_JOIN_LABEL="JOIN ROOM"
```

---

2. **By modifying the HTML files** with `BRAND_HTML_INJECTION` disabled

In this approach, brand injection is disabled and you can fully customize the project for your needs. The frontend files are located in the `app/public/views` folder.

---

## Reference

The full environment configuration can be found [here](https://github.com/miroslavpejic85/mirotalksfu/blob/main/.env.template)

## Configuration Note

MiroTalk SFU uses environment variables defined in `.env` (based on .env.template) to configure all core services: signaling, media transport, and more.

The entry point [config.js]() automatically loads these variables and exposes them to the app.
You should not modify `config.js`; instead, edit the `.env` file.

---

## Updates (self-hosted)

When you update to the newest version of MiroTalk SFU using the `./sfuUpdate.sh` script, any customized files (such as your branding in public/views) get overwritten. This happens because the update process replaces the entire base code and can’t automatically preserve client-specific modifications.

So after each update, you’ll need to reapply your own branding files unless they’re separated from the tracked source code and also if there are changes in the `.env - config.js` file need to update it as well accordingly.

Here are a few recommended options to handle this more smoothly:

### ✅ Option 1: Use `git stash` before updating

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

### ✅ Option 2: Create a dedicated `“custom-branding” branch`

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

### ✅ Option 3: Mount your branding via `Docker volumes`

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