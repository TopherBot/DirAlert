#!/usr/bin/env python3
import os
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import requests

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

class NewFileHandler(FileSystemEventHandler):
    def __init__(self, bot_token, chat_id):
        self.bot_token = bot_token
        self.chat_id = chat_id

    def on_created(self, event):
        if event.is_directory:
            return
        filename = os.path.basename(event.src_path)
        message = f"🆕 New file created: {filename}"
        self.send_telegram(message)

    def send_telegram(self, text):
        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
        payload = {"chat_id": self.chat_id, "text": text}
        try:
            r = requests.post(url, json=payload, timeout=5)
            r.raise_for_status()
            logging.info("Telegram alert sent")
        except Exception as e:
            logging.error(f"Failed to send Telegram: {e}")

def main():
    watch_path = os.getenv('WATCH_PATH')
    bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')

    if not all([watch_path, bot_token, chat_id]):
        logging.error("Please set WATCH_PATH, TELEGRAM_BOT_TOKEN, and TELEGRAM_CHAT_ID env vars.")
        sys.exit(1)

    event_handler = NewFileHandler(bot_token, chat_id)
    observer = Observer()
    observer.schedule(event_handler, watch_path, recursive=False)
    observer.start()
    logging.info(f"Monitoring {watch_path} ...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()
