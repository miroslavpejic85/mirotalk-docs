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
    npm install
    npm start
    ```

2. **Open the Admin Dashboard**

    - Go to: [http://localhost:9999/admin](http://localhost:9999/admin)
    - **Default credentials:**
        - **Username:** `admin`
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
    npm install
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

## ⚠️ Security Checklist

> **Important:**  
> Before using MiroTalk Admin, update your environment settings to keep your instance secure.

### 🔐 Admin Dashboard

- Set `ADMIN_DASHBOARD_ENABLED=true` to enable the dashboard.
- **Change the default credentials:**
    - `ADMIN_USERNAME`
    - `ADMIN_PASSWORD`
    - `ADMIN_JWT_SECRET`

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

---

> ✅ **Tip:**  
> Regularly review and update your `.env` settings to keep your MiroTalk instance secure and manageable.

---
