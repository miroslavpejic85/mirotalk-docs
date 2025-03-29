# **Configuration Files Overview**

![settings](../images/settings.png)

This system relies on one primary configuration file for customization:

!!! warning "Configuration Required"
    **Before proceeding, ensure you've copied these critical file:**  

    - 🔧 `.env.template` → `.env`  

    **Failure to do this will cause application errors.** 

1. **[`.env`](https://github.com/miroslavpejic85/mirotalkc2c/blob/main/.env.template)**  
      - Stores sensitive credentials and environment-specific variables.  
      - Should always be included in `.gitignore` to prevent accidental commits to version control.  

## **Best Practices:**   
- Store secrets and environment-specific variables exclusively in `.env`.   
- Secure the `.env` file by restricting access and including it in `.gitignore`.