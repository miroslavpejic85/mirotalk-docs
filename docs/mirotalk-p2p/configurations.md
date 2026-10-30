# **Configuration Files Overview**

![settings](../images/settings.png)

MiroTalk P2P uses `app/src/config.js` for application configuration and `.env` for environment-specific settings. The config template reads environment variables and supplies defaults; `.env` includes both sensitive values and non-sensitive options such as branding and UI behavior.

!!! warning "Configuration Required"
    **Before proceeding, create these local configuration files from their templates:**

    - 📄 `app/src/config.template.js` → `app/src/config.js`  
    - 🔧 `.env.template` → `.env`  

    Keep the local files private and compare them with the latest templates when updating.

1. **[`config.js`](https://github.com/miroslavpejic85/mirotalk/blob/master/app/src/config.template.js)**  
      - Application configuration and defaults; reads environment variables from `.env`.
      - Keep it based on the latest template so it recognizes newly added settings.

2. **[`.env`](https://github.com/miroslavpejic85/mirotalk/blob/master/.env.template)**  
      - Stores secrets and environment-specific settings, including P2P branding and UI options.
      - Keep it private and out of version control.

## **Best Practices:**  
- Use `.env` for environment values and UI customization; see the [rebranding guide](rebranding.md) for branding options.
- Keep `config.js` based on the current template and use it for application configuration that is not exposed as an environment variable.
- Consult the comments in both templates for available settings and defaults.
- Restrict access to `.env` and ensure it is not committed to version control.