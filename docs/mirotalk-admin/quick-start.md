# MiroTalk Admin

A secure, modern web dashboard to manage **[MiroTalk](https://docs.mirotalk.com/html/overview.html)** updates, configuration, and settings with ease.

---

![admin](../images/mirotalk/adm.png)

---

## 🚀 Quick Start

1. **Clone the Repository and Set Up Backend**

    ```bash
    git clone https://github.com/miroslavpejic85/mirotalk-admin.git
    cd mirotalk-admin
    cp backend/config/index.template.js backend/config/index.js
    cp .env.template .env
    npm ci
    npm start
    ```

2. **Open the Admin Dashboard**

    - Go to: [http://localhost:9999/admin](http://localhost:9999/admin)
    - **Default credentials:**
        - **Username:** `mirotalk`
        - **Password:** `admin`

---

## ⚡ Quick Start with PM2

1. **Install PM2 globally (if not already installed):**

    ```bash
    npm install -g pm2
    ```

2. **Clone and set up the project:**

    ```bash
    git clone https://github.com/miroslavpejic85/mirotalk-admin.git
    cd mirotalk-admin
    cp backend/config/index.template.js backend/config/index.js
    cp .env.template .env
    npm ci
    ```

3. **Start the server with PM2:**

    ```bash
    pm2 start backend/server.js --name mirotalk-admin
    ```

4. **View logs and manage the process:**

    ```bash
    pm2 logs mirotalk-admin
    pm2 status
    ```

5. **Access the Dashboard:**
    - Open: [http://localhost:9999/admin](http://localhost:9999/admin)

---

## 🐳 Quick Start with Docker

!!! warning
    **Works only on `APP_MANAGE_MODE=ssh`**

1. **Prepare Your Environment Files**

    ```bash
    git clone https://github.com/miroslavpejic85/mirotalk-admin.git
    cd mirotalk-admin
    cp backend/config/index.template.js backend/config/index.js
    cp .env.template .env
    cp docker-compose.template.yml docker-compose.yml
    ```

2. **Pull and Run with Docker Compose**

    ```bash
    docker pull mirotalk/admin:latest
    docker compose up
    ```

3. **Access the Dashboard**
    - Open: [http://localhost:9999/admin](http://localhost:9999/admin)

---

## ⚠️ Security Checklist

> **Important:**  
> Before using MiroTalk Admin, update your environment settings to keep your instance secure.

### 🔐 Admin Dashboard

- Set `ADMIN_DASHBOARD_ENABLED=true` to enable the dashboard.
- **Change the default credentials:**
    - `ADMIN_USERNAME`
    - `ADMIN_PASSWORD_HASH`  

        👉 generate it by running:

        ```js
        node backend/scripts/hashPassword.js
        ```

    - `ADMIN_JWT_SECRET` 
  
        👉 generate it by running:

        ```js
        node backend/scripts/generateJwtSecret.js
        ```

### 🛠️ Management Mode (`APP_MANAGE_MODE`)

Choose how you want to manage your MiroTalk instance:

- **Local Device Management (via SSH):**

    - Set `APP_MANAGE_MODE=ssh`
    - Configure:
        - `SSH_HOST`
        - `SSH_PORT`
        - `SSH_USERNAME`
        - `SSH_PASSWORD` or `SSH_PRIVATE_KEY`

- **Self-Hosted with Docker:**

    - Set `APP_MANAGE_MODE=docker`

- **Self-Hosted with PM2:**
    - Set `APP_MANAGE_MODE=pm2`

Specify which instances you want to manage by listing their names (comma-separated), and provide the absolute paths to their directories:

```bash
APP_NAME=mirotalksfu,mirotalk,mirotalkc2c,mirotalkbro,mirotalkwebrtc,mirotalkadmin
MIROTALK_SFU_DIR=/root/mirotalksfu
MIROTALK_P2P_DIR=/root/mirotalk
MIROTALK_BRO_DIR=/root/mirotalkbro
MIROTALK_C2C_DIR=/root/mirotalkc2c
MIROTALK_WEB_DIR=/root/mirotalkwebrtc
MIROTALK_ADMIN_DIR=/root/mirotalk-admin
```

---

> ✅ **Tip:**  
> Regularly review and update your `.env` settings to keep your MiroTalk instance secure and manageable.

---
