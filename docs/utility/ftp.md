# Enabling FTP on Ubuntu 22.04 LTS

![ftp](../images/ftp.png)

Install the FTP Server, For this example, we'll use `vsftpd`, a popular and secure FTP server

## Set up an FTP server using `vsftpd`

```bash
# Update Package Lists
$ sudo apt update

# Install the FTP Server
$ sudo apt install vsftpd

# Start and Enable the FTP Service
$ sudo systemctl start vsftpd
$ sudo systemctl enable vsftpd
```

## Configure the FTP Server

Edit the `vsftpd` configuration file

```bash
$ sudo vim /etc/vsftpd.conf #(:i)
```

Adjust the following settings:

```conf
# Disable Anonymous Access
anonymous_enable=NO

# Allow Local Users to Log In
local_enable=YES

# Enable File Uploads
write_enable=YES

# Restrict Users to Their Home Directories
chroot_local_user=YES
```

Save the file and exit (:wq).

## Restart the FTP Service

Apply the changes by restarting the `vsftpd` service:

```bash
$ sudo systemctl restart vsftpd
```

## Configure the Firewall (if applicable)

Allow FTP traffic through the firewall:

```bash
$ sudo ufw status
$ sudo ufw allow 21/tcp
```

## Test the FTP Connection

Use an FTP client or the command-line tool to test the connection. For command-line testing:

```bash
$ ftp <server_ip_address>
```

Replace `<server_ip_address>` with your server’s IP address.

Or using the FTP client: [FileZilla Client](https://filezilla-project.org/)
