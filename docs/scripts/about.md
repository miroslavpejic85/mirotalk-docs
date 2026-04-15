# **MiroTalk Setup Guide**

![setup](../images/self-hosting.png)

## **Requirements**

*  A clean server running **Ubuntu 22.04 or 24.04 LTS**
*  **Root access** to the Server
*  A **domain or subdomain** pointing to your server’s public IPv4

---

## Note

When **prompted**, simply **enter your domain or subdomain**. Then wait for the installation to complete.

---

## **MiroTalk SFU**

```bash
# Install MiroTalk SFU
wget -qO sfu-install.sh https://docs.mirotalk.com/scripts/sfu/sfu-install.sh \
  && chmod +x sfu-install.sh \
  && ./sfu-install.sh
```
```bash
# Uninstall MiroTalk SFU
wget -qO sfu-uninstall.sh https://docs.mirotalk.com/scripts/sfu/sfu-uninstall.sh \
  && chmod +x sfu-uninstall.sh \
  && ./sfu-uninstall.sh
```
```bash
# Update MiroTalk SFU
wget -qO sfu-update.sh https://docs.mirotalk.com/scripts/sfu/sfu-update.sh \
  && chmod +x sfu-update.sh \
  && ./sfu-update.sh
```

---

## **MiroTalk P2P**

```bash
# Install MiroTalk P2P
wget -qO p2p-install.sh https://docs.mirotalk.com/scripts/p2p/p2p-install.sh \
  && chmod +x p2p-install.sh \
  && ./p2p-install.sh
```
```bash
# Uninstall MiroTalk P2P
wget -qO p2p-uninstall.sh https://docs.mirotalk.com/scripts/p2p/p2p-uninstall.sh \
  && chmod +x p2p-uninstall.sh \
  && ./p2p-uninstall.sh
```
```bash
# Update MiroTalk P2P
wget -qO p2p-update.sh https://docs.mirotalk.com/scripts/p2p/p2p-update.sh \
  && chmod +x p2p-update.sh \
  && ./p2p-update.sh
```

---

## **MiroTalk C2C**

```bash
# Install MiroTalk C2C
wget -qO c2c-install.sh https://docs.mirotalk.com/scripts/c2c/c2c-install.sh \
  && chmod +x c2c-install.sh \
  && ./c2c-install.sh
```
```bash
# Uninstall MiroTalk C2C
wget -qO c2c-uninstall.sh https://docs.mirotalk.com/scripts/c2c/c2c-uninstall.sh \
  && chmod +x c2c-uninstall.sh \
  && ./c2c-uninstall.sh
```
```bash
# Update MiroTalk C2C
wget -qO c2c-update.sh https://docs.mirotalk.com/scripts/c2c/c2c-update.sh \
  && chmod +x c2c-update.sh \
  && ./c2c-update.sh
```

---

## **MiroTalk BRO**

```bash
# Install MiroTalk BRO
wget -qO bro-install.sh https://docs.mirotalk.com/scripts/bro/bro-install.sh \
  && chmod +x bro-install.sh \
  && ./bro-install.sh
```
```bash
# Uninstall MiroTalk BRO
wget -qO bro-uninstall.sh https://docs.mirotalk.com/scripts/bro/bro-uninstall.sh \
  && chmod +x bro-uninstall.sh \
  && ./bro-uninstall.sh
```
```bash
# Update MiroTalk BRO
wget -qO bro-update.sh https://docs.mirotalk.com/scripts/bro/bro-update.sh \
  && chmod +x bro-update.sh \
  && ./bro-update.sh
```

---

## **MiroTalk WEB**

```bash
# Install MiroTalk WEB
wget -qO web-install.sh https://docs.mirotalk.com/scripts/web/web-install.sh \
  && chmod +x web-install.sh \
  && ./web-install.sh
```
```bash
# Uninstall MiroTalk WEB
wget -qO web-uninstall.sh https://docs.mirotalk.com/scripts/web/web-uninstall.sh \
  && chmod +x web-uninstall.sh \
  && ./web-uninstall.sh
```
```bash
# Update MiroTalk WEB
wget -qO web-update.sh https://docs.mirotalk.com/scripts/web/web-update.sh \
  && chmod +x web-update.sh \
  && ./web-update.sh
```

---

## **MiroTalk CME**

```bash
# Install MiroTalk CME
wget -qO cme-install.sh https://docs.mirotalk.com/scripts/cme/cme-install.sh \
  && chmod +x cme-install.sh \
  && ./cme-install.sh
```
```bash
# Uninstall MiroTalk CME
wget -qO cme-uninstall.sh https://docs.mirotalk.com/scripts/cme/cme-uninstall.sh \
  && chmod +x cme-uninstall.sh \
  && ./cme-uninstall.sh
```
```bash
# Update MiroTalk CME
wget -qO cme-update.sh https://docs.mirotalk.com/scripts/cme/cme-update.sh \
  && chmod +x cme-update.sh \
  && ./cme-update.sh
```

---

## **Coturn**

```bash
# Install Coturn
wget -qO coturn-install.sh https://docs.mirotalk.com/scripts/coturn/coturn-install.sh \
  && chmod +x coturn-install.sh \
  && ./coturn-install.sh
```
```bash
# Uninstall Coturn
wget -qO coturn-uninstall.sh https://docs.mirotalk.com/scripts/coturn/coturn-uninstall.sh \
  && chmod +x coturn-uninstall.sh \
  && ./coturn-uninstall.sh
```