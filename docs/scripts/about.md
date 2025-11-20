# **MiroTalk Setup Guide**

![setup](../images/globe.png)

## **Requirements**

*  A clean server running **Ubuntu 22.04 or 24.04 LTS**
*  **Root access** to the Server
*  A **domain or subdomain** pointing to your server’s public IPv4

---

## Note

When **prompted**, simply **enter your domain or subdomain**. Then wait for the installation to complete.

---

## **Install**

```bash
# Install MiroTalk SFU
wget -qO sfu-install.sh https://docs.mirotalk.com/scripts/sfu/sfu-install.sh \
  && chmod +x sfu-install.sh \
  && ./sfu-install.sh
```
```bash
# Install MiroTalk P2P
wget -qO p2p-install.sh https://docs.mirotalk.com/scripts/p2p/p2p-install.sh \
  && chmod +x p2p-install.sh \
  && ./p2p-install.sh
```
```bash
# Install MiroTalk C2C
wget -qO c2c-install.sh https://docs.mirotalk.com/scripts/c2c/c2c-install.sh \
  && chmod +x c2c-install.sh \
  && ./c2c-install.sh
```
```bash
# Install MiroTalk BRO
wget -qO bro-install.sh https://docs.mirotalk.com/scripts/bro/bro-install.sh \
  && chmod +x bro-install.sh \
  && ./bro-install.sh
```
```bash
# Install Coturn
wget -qO coturn-install.sh https://docs.mirotalk.com/scripts/coturn/coturn-install.sh \
  && chmod +x coturn-install.sh \
  && ./coturn-install.sh
```

---

## **Uninstall**

```bash
# Uninstall MiroTalk SFU
wget -qO sfu-uninstall.sh https://docs.mirotalk.com/scripts/sfu/sfu-uninstall.sh \
  && chmod +x sfu-uninstall.sh \
  && ./sfu-uninstall.sh
```
```bash
# Uninstall MiroTalk P2P
wget -qO p2p-uninstall.sh https://docs.mirotalk.com/scripts/p2p/p2p-uninstall.sh \
  && chmod +x p2p-uninstall.sh \
  && ./p2p-uninstall.sh
```
```bash
# Uninstall MiroTalk C2C
wget -qO c2c-uninstall.sh https://docs.mirotalk.com/scripts/c2c/c2c-uninstall.sh \
  && chmod +x c2c-uninstall.sh \
  && ./c2c-uninstall.sh
```
```bash
# Uninstall MiroTalk BRO
wget -qO c2c-uninstall.sh https://docs.mirotalk.com/scripts/bro/bro-uninstall.sh \
  && chmod +x bro-uninstall.sh \
  && ./bro-uninstall.sh
```
```bash
# Uninstall Coturn
wget -qO coturn-uninstall.sh https://docs.mirotalk.com/scripts/coturn/coturn-uninstall.sh \
  && chmod +x coturn-uninstall.sh \
  && ./coturn-uninstall.sh
```

---

## Updates

```bash
# Update MiroTalk SFU
wget -qO sfu-update.sh https://docs.mirotalk.com/scripts/sfu/sfu-update.sh \
  && chmod +x sfu-update.sh \
  && ./sfu-update.sh
```
```bash
# Update MiroTalk P2P
wget -qO p2p-update.sh https://docs.mirotalk.com/scripts/p2p/p2p-update.sh \
  && chmod +x p2p-update.sh \
  && ./p2p-update.sh
```
```bash
# Update MiroTalk C2C
wget -qO c2c-update.sh https://docs.mirotalk.com/scripts/c2c/c2c-update.sh \
  && chmod +x c2c-update.sh \
  && ./c2c-update.sh
```
```bash
# Update MiroTalk BRO
wget -qO bro-update.sh https://docs.mirotalk.com/scripts/bro/bro-update.sh \
  && chmod +x bro-update.sh \
  && ./bro-update.sh
```