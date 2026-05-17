# DirAlert

A tiny Python utility that watches a directory and sends a Telegram message whenever a new file is created.

## Features

- Monitors a folder in real‑time.
- Sends instant alerts via Telegram bot.
- Configurable via environment variables.
- Zero‑dependency aside from the watchdog library.

## Installation

```bash
pip install watchdog requests
```

## Usage

Set the required environment variables:

- `WATCH_PATH` – Path of the directory to monitor.
- `TELEGRAM_BOT_TOKEN` – Token of your Telegram bot.
- `TELEGRAM_CHAT_ID` – Chat ID where messages will be sent.

Run the script:

```bash
python monitor.py
```

## Example

```bash
export WATCH_PATH=/home/user/downloads
export TELEGRAM_BOT_TOKEN=123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11
export TELEGRAM_CHAT_ID=987654321
python monitor.py
```

The script will now send a Telegram message each time a new file appears in the watched folder.

## License

MIT
