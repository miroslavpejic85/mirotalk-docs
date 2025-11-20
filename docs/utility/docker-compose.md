# Update to latest docker-compose

Repo: [https://github.com/docker/compose/releases/](https://github.com/docker/compose/releases/)

```bash
# Remove any existing installation of docker-compose
$ sudo apt remove docker-compose

# Download the latest version of docker-compose (v2.40.3 in this case) for Linux (x86_64 architecture)
$ wget https://github.com/docker/compose/releases/download/v2.40.3/docker-compose-linux-x86_64

# Make the downloaded docker-compose file executable
$ chmod +x docker-compose-linux-x86_64

# Move the docker-compose binary to /usr/bin to make it globally accessible
$ sudo mv docker-compose-linux-x86_64 /usr/bin/docker-compose

# Verify the installed version of docker-compose
$ docker-compose --version
```