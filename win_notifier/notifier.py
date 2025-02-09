import json
import time
from win10toast import ToastNotifier

toaster = ToastNotifier()

def send_notification(message):
    toaster.show_toast("Home Assistant", message, duration=5)

while True:
    try:
        with open("notification.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            send_notification(data.get("message", "No message"))
    except Exception as e:
        send_notification(f"Error: {str(e)}")
    time.sleep(10)
