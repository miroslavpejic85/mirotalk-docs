# **Configuration Files Overview**

![settings](../images/settings.png)

This system relies on two primary configuration files for customization:

!!! warning "Configuration Required"
    **Before proceeding, ensure you've copied these critical files:**  

    - 🔧 `.env.template` → `.env`  
    - 🔧 `frontend/js/config.template.js` → `frontend/js/config.js`  

    **Failure to do this will cause application errors.** 

1. **[`config.js`](https://github.com/miroslavpejic85/mirotalkc2c/blob/main/frontend/js/config.template.js)**  
      - Contains non-sensitive UI settings (app name, copyright, about link).  
      - Sent to the browser, so never put secrets in it.  
      - Git-ignored, so your customizations survive updates. If missing, `config.template.js` is served instead.  

2. **[`.env`](https://github.com/miroslavpejic85/mirotalkc2c/blob/main/.env.template)**  
      - Stores sensitive credentials and environment-specific variables.  
      - Should always be included in `.gitignore` to prevent accidental commits to version control.  

## **Best Practices:**   
- Use `config.js` only for non-sensitive, browser-visible UI settings.   
- Store secrets and environment-specific variables exclusively in `.env`.   
- Secure the `.env` file by restricting access and including it in `.gitignore`.