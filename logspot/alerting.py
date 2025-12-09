import requests
import os
from dotenv import load_dotenv
load_dotenv()

def send_telegram(msg: str, chat_id: str | None, bot_token: str) -> bool: 
    """
    Send message to a specific Telegram chat_id using the given bot_token.
    Both chat_id and bot_token MUST be provided by caller.
    """
    if not bot_token:
        print("Telegram Bot Token not set.")
        return False

    if not chat_id:
        print("No chat_id provided for Telegram message")
        return False

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
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
