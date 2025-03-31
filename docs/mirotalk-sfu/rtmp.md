# MiroTalk RTMP Servers

![rtmp](../images/rtmp.jpeg)

We introduced two types of RTMP (Real-Time Messaging Protocol) servers: **[Node Media Server](https://github.com/illuspas/Node-Media-Server)** and **[Nginx RTMP](https://github.com/tiangolo/nginx-rtmp-docker)**. These servers handle streaming media efficiently, making them suitable for applications like MiroTalk SFU (Selective Forwarding Unit).

---

## Prerequisites

```bash
$ sudo apt update

# Install docker
$ sudo apt install -y docker.io

# Instal docker-compose
$ sudo apt install -y docker-compose

# Install ffmpeg
$ sudo apt install -y ffmpeg
```

---

## Node Media Server

Node Media Server uses Node.js to handle RTMP streaming efficiently, suitable for applications like MiroTalk SFU.

### Setup Instructions

1. **Create a rtmp Directory:**
	```bash
	$ mkdir app/rtmp
	```

2. **Navigate to Server Directory:**
	```bash
	$ cd rtmpServers/node-media-server
	```

3. **Configure Server:**
   ```bash
   $ cp src/config.template.js src/config.js
   ```

4. **Set Up Docker:**
   ```bash
   $ cp docker-compose.template.yml docker-compose.yml

   $ docker pull mirotalk/nms:latest

   $ cd ../..
   ```

5. **Manage Server:**
   ```bash
   # Start Node Media Server
   $ npm run nms-start

   # Stop Node Media Server
   $ npm run nms-stop

   # Restart Node Media Server
   $ npm run nms-restart

   # Check Server Logs
   $ npm run nms-logs
   ```

6. **Admin dashboard**: `https://your-domain-name:8043/admin`  
   **Api server**: `https://your-domain-name:8043/api/server`  
   **Api streams**: `https://your-domain-name:8043/api/streams`

---

## Nginx RTMP

Nginx RTMP adds RTMP streaming support to the Nginx web server and reverse proxy.

### Setup Instructions

1. **Create a rtmp Directory:**
	```bash
	$ mkdir app/rtmp
	```

2. **Navigate to Server Directory:**
   ```bash
   $ cd rtmpServers/nginx-rtmp
   ```

3. **Set Up Docker:**
   ```bash
   $ cp docker-compose.template.yml docker-compose.yml

   $ docker pull mirotalk/rtmp:latest

   $ cd ../..
   ```

4. **Manage Server:**
   ```bash
   # Start Nginx RTMP Server
   $ npm run rtmp-start

   # Stop Nginx RTMP Server
   $ npm run rtmp-stop

   # Restart Nginx RTMP Server
   $ npm run rtmp-restart

   # Check Server Logs
   $ npm run rtmp-logs
   ```

5. **Check stat:**: `https://your-domain-name:1935/stat`

---

## Demo Projects

Explore our **[2 RTMP Servers](https://github.com/miroslavpejic85/mirotalksfu/tree/main/rtmpServers)** to test your RTMP capabilities:

### 1. Client-Server-Axios  
- **Method:** POST  
- **Description:** Uses **[Axios](https://axios-http.com)** for HTTP communication.  

### 2. Client-Server-Socket  
- **Technology:** **[Socket.io](https://socket.io)**  
- **Description:** Enables real-time communication via WebSockets.  

Try them out to see how they integrate with your RTMP workflow!  

---

## Using OBS with RTMP Server

To stream from **[OBS](https://obsproject.com)** (Open Broadcaster Software) to an MiroTalk RTMP server:

### Configure Stream Settings:

- Go to **Settings**.
- Select **Stream**.
- Set **Service** to **Custom...**.
- Enter **Server** as `rtmp://your-domain-name:1935/live`.
- Use a unique **Stream key**, e.g., `something-random`.

### Start Streaming:

- Start streaming from OBS.
- Share your RTMP URL: `rtmp://your-domain-name:1935/live/something-random`.

---

!!! note

      If your `Node Media Server` has authentication enabled with the following settings:

      ```javascript
      auth: {
         play: true, // Require authentication for playing streams
         publish: true, // Require authentication for publishing streams
         secret: 'mirotalkRtmpSecret' // Secret key used for generating a valid RTMP URL
      },
      ```

      You need to generate a valid RTMP URL using the `sign.js` script. Follow these steps:

      1. Run the `sign.js` script to generate a valid RTMP URL:
         ```sh
         node sign.js
         ```

      2. The generated URL will look like this:
         ```
         rtmp://your-domain-name:1935/live/something-random?sigh=xxxxxx-xxxxxxxxxxxxxxxxxxxxxx
         ```

      Replace `your-domain-name`, `something-random`, and `xxxxxx-xxxxxxxxxxxxxxxxxxxxxx` with the appropriate values.

---
