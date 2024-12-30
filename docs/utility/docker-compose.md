# Update to latest docker-compose

Repo: [https://github.com/docker/compose/releases/](https://github.com/docker/compose/releases/)

```bash
sudo apt remove docker-compose
wget https://github.com/docker/compose/releases/download/v2.32.1/docker-compose-linux-x86_64
chmod +x docker-compose-linux-x86_64
sudo mv docker-compose-linux-x86_64 /usr/bin/docker-compose
docker-compose --version
```