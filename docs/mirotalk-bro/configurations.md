# **Configuration Files Overview**

![settings](../images/settings.png)

This system relies on two primary configuration files for customization:  

!!! warning "Configuration Required"
    **Before proceeding, ensure you've copied these critical files:**  
 
    - 🔧 `.env.template` → `.env`  
    - 🔧 `public/js/config.template.js` → `public/js/config.js`  

    **Failure to do this will cause application errors.** 

1. **[`config.js`](https://github.com/miroslavpejic85/mirotalkbro/blob/main/public/js/config.template.js)**  
      - Contains all non-sensitive application settings with detailed, in-line documentation.  
      - Ideal for configuring general application behavior and features.  
      - Git-ignored, so your customizations survive updates. If missing, `config.template.js` is served instead.  

2. **[`.env`](https://github.com/miroslavpejic85/mirotalkbro/blob/main/.env.template)**  
      - Stores sensitive credentials and environment-specific variables.  
      - Should always be included in `.gitignore` to prevent accidental commits to version control.  

## **Best Practices:**  
- Utilize `config.js` for non-sensitive, general application settings.  
- Store secrets and environment-specific variables exclusively in `.env`.  
- Consult the documentation comments within `config.js` for detailed configuration guidance.  
- Secure the `.env` file by restricting access and including it in `.gitignore`.