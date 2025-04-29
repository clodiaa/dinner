import requests
from datetime import date

# Telegram Bot details
BOT_TOKEN = "7994330393:AAGdVFaEI1Ey4MTQvCJfvk4_v1BuqxCy-tM"
CHAT_ID = "-4762617003"  # Replace with your group chat ID

# Get today's date
today = date.today().strftime("%A, %d %B %Y")  # e.g., Monday, 29 April 2025

# Message with inline buttons (asking whether person A and person B are eating dinner)
message = f"""
Eating dinner tonight? ({today})

Person A: ✅ Yes / ❌ No
Person B: ✅ Yes / ❌ No
"""

# Inline keyboard buttons for Person A and Person B responses
keyboard = {
    "inline_keyboard": [
        [
            {"text": "Person A: ✅ Yes", "callback_data": "person_a_yes"},
            {"text": "Person A: ❌ No", "callback_data": "person_a_no"}
        ],
        [
            {"text": "Person B: ✅ Yes", "callback_data": "person_b_yes"},
            {"text": "Person B: ❌ No", "callback_data": "person_b_no"}
        ]
    ]
}

# Telegram API URL
url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

# Payload for the request
payload = {
    "chat_id": CHAT_ID,
    "text": message,
    "reply_markup": keyboard  # Add the inline keyboard to the message
}

# Sending the message
response = requests.post(url, json=payload)

# Log the response from Telegram API
print("Status:", response.status_code)
print("Response:", response.text)
