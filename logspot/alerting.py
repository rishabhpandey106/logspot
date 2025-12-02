import requests
import os
from dotenv import load_dotenv
load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

def send_telegram(msg: str, chat_id: str | None) -> bool: 
    """Send message to a specific Telegram chat_id."""
    if not TELEGRAM_BOT_TOKEN:
        print("Telegram Bot Token not set.")
        return False

    if not chat_id:
        print("No chat_id provided for Telegram message")
        return False

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": msg,
        "disable_web_page_preview": True,
    }

    try:
        response = requests.post(url, data=data, timeout=5)
        print(f"Telegram API Response: {response.text}")
        if response.status_code == 200:
            print("Telegram notification sent successfully.")
            return True
        else:
            print(f"Failed to send message: {response.text}")
            return False
    except Exception as e:
        print(f"Error sending Telegram message: {e}")
        return False
