import requests

BOT_TOKEN = "7994330393:AAGdVFaEI1Ey4MTQvCJfvk4_v1BuqxCy-tM"
CHAT_ID = "-4762617003"
MESSAGE = "Hello! This is your daily message."

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
payload = {"chat_id": CHAT_ID, "text": MESSAGE}

response = requests.post(url, data=payload)
print("Status:", response.status_code)
print("Response:", response.text)
