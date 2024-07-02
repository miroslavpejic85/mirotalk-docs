# MiroTalk RTMP Servers

![rtmp](../images/rtmp.jpeg)

We introduced two types of RTMP (Real-Time Messaging Protocol) servers: **[Node Media Server](https://github.com/illuspas/Node-Media-Server)** and **[Nginx RTMP](https://github.com/tiangolo/nginx-rtmp-docker)**. These servers handle streaming media efficiently, making them suitable for applications like MiroTalk SFU (Selective Forwarding Unit).

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

## Node Media Server

Node Media Server uses Node.js to handle RTMP streaming efficiently, suitable for applications like MiroTalk SFU.

### Setup Instructions

1. **Navigate to Server Directory:**
	```bash
	$ cd rtmpServers/node-media-server
	```

2. **Configure Server:**
   ```bash
   $ cp config.template.js config.js
   ```

3. **Set Up Docker:**
   ```bash
   $ cp docker-compose.template.yml docker-compose.yml

   $ docker pull mirotalk/nms:latest

   $ cd ../..
   ```

4. **Manage Server:**
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

5. **Admin dashboard**: `https://your-domain-name:8043/admin`  
   **Api server**: `https://your-domain-name:8043/api/server`  
   **Api streams**: `https://your-domain-name:8043/api/streams`

## Nginx RTMP

Nginx RTMP adds RTMP streaming support to the Nginx web server and reverse proxy.

### Setup Instructions

1. **Navigate to Server Directory:**
   ```bash
   $ cd rtmpServers/nginx-rtmp
   ```

2. **Set Up Docker:**
   ```bash
   $ cp docker-compose.template.yml docker-compose.yml

   $ docker pull mirotalk/rtmp:latest

   $ cd ../..
   ```

3. **Manage Server:**
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

4. **Check stat:**: `https://your-domain-name:1935/stat`

## Demo Projects

Explore our 2 demo projects designed to test your RTMP capabilities:

### client-server-axios
- Method: POST
- Description: This project utilizes **[Axios](https://axios-http.com)** for communication.

### client-server-socket
- Technology: **[socket.io](https://socket.io)**
- Description: This project uses socket.io for real-time communication.

Feel free to try them out and see how they work with your RTMP setup!

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
