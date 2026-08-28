<p align="center">
    <a href="https://docs.mirotalk.com"><img src="docs/images/mirotalk-preview.png" alt="MiroTalk WebRTC documentation"></a>
</p>

<h1 align="center">MiroTalk DOCS</h1>

<br />

<p align="center">MiroTalk WebRTC is a real-time communication technology that enables audio and video communication over the internet through web browsers without the need for additional plugins or software installations. It stands out as a core component of many web-based video conferencing and communication platforms. Here you will find all the necessary documentations.</p>

<hr />

<p align="center">
    <a href="https://docs.mirotalk.com">Explore MiroTalk DOCS</a>
</p>

<hr />

## Installation

### Using a virtual environment (recommended)

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

With fish shell, activate the environment with:

```fish
source .venv/bin/activate.fish
```

---

## Quick Start

```bash
# Clone the repo
$ git clone https://github.com/miroslavpejic85/mirotalk-docs.git

# Go to Docs dir
$ cd mirotalk-docs

# Create and activate a virtual environment
$ python3 -m venv .venv
$ source .venv/bin/activate

# Install the documentation dependencies
$ python -m pip install -r requirements.txt

# Start the built-in dev-server
$ python -m mkdocs serve
```

Open up [http://127.0.0.1:8000](http://127.0.0.1:8000/) in your browser.

---

## Self hosting

[Here the documentation](./docs/docs/self-hosting.md)

---

## Credits

- **[MkDocs](https://github.com/mkdocs/mkdocs)**
- **[MkDocs-material](https://github.com/squidfunk/mkdocs-material)**
