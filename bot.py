---
## 1️⃣ فایل bot.py
```python
import requests
import time
import json


API = "https://messengerg2c63.iranlms.ir"


with open("config.json") as f:
config = json.load(f)
TOKEN = config["token"]


HEADERS = {
"Content-Type": "application/json"
}


def send_message(chat_id, text):
data = {
"api_version": "0",
"auth": TOKEN,
"data": {
"chat_id": chat_id,
"text": text
}
}
requests.post(f"{API}/sendMessage", json=data, headers=HEADERS)


last_update = None


while True:
data = {
"api_version": "0",
"auth": TOKEN,
"data": {"last_update_id": last_update}
}


res = requests.post(f"{API}/getUpdates", json=data).json()


for update in res.get("data", {}).get("updates", []):
last_update = update["update_id"]
msg = update.get("message")
if not msg: continue


chat_id = msg["chat_id"]
text = msg.get("text", "")


if text == "/start":
send_message(chat_id, "سلام! ربات روبیکا فعال شد 🤖")
elif text == "سلام":
send_message(chat_id, "سلام رفیق 😎")


time.sleep(3)
