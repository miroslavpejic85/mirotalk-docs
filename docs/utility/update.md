# System Update Script

This script will update your Ubuntu/Debian system and display OS information.

## 📋 Script

```bash
#!/bin/bash

sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get dist-upgrade -y

lsb_release -a
```

---

## 🚀 How to Use

1. **Save the script above as `update.sh`.**
2. **Make it executable:**
    ```bash
    chmod +x update.sh
    ```
3. **Run the script:**
    ```bash
    ./update.sh
    ```

---

!!! note

	After running, A reboot may or may not be necessary:
	```bash
	sudo reboot
	```