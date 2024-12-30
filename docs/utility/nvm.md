# Node Version Manager (NVM)

![nvm](../images/nvm.png)

Here's a step-by-step guide on how to use [NVM](https://github.com/nvm-sh/nvm) (Node Version Manager) to install and manage specific versions of Node.js on your system:

## Install NVM

If you haven't already installed NVM, you can do so by running the following command in your terminal:

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
```

Or, if you prefer using Wget:

```bash
wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
```

This command will install NVM on your system. You may need to restart your terminal or run `source ~/.bashrc` (or `~/.zshrc` if you use Zsh) to start using NVM.

## Check NVM Version

You can verify that NVM has been installed correctly by typing:

```bash
nvm --version
```

## List available Node.js versions

You can list the available Node.js versions by running:

```bash
nvm ls-remote
```

This should display the version of NVM that you installed.

## Install a Specific Version of Node.js

To install a specific version of Node.js, use the following command:

```bash
nvm install X.X.X
```

Replace `X.X.X` with the version number you want to install. For example, to install Node.js version `18.18.2`:

```bash
nvm install 18.20.5
```

## Use the Installed Node.js Version

Once the installation is complete, you can use the installed version by typing:

```bash
nvm use X.X.X
```

For example:

```bash
nvm use 18.20.5
```

You can check the current Node.js version in use with:

```bash
node -v
```

## Set a Default Node.js Version (Optional)

If you want to set a default Node.js version to be used in new shell sessions, you can type:

```bash
nvm alias default X.X.X
```

For example, to set version `18.18.2` as the default:

```bash
nvm alias default 18.18.2
```

Now you have successfully installed and managed a specific version of Node.js using NVM.
Remember that you can always switch to different versions using the `nvm use` command.

---
