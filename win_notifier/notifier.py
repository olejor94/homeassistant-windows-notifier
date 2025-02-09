from win10toast import ToastNotifier
import json
import time

toaster = ToastNotifier()

def send_notification(message):
    toaster.show_toast("Home Assistant", message, duration=5)

while True:
    with open("notification.json", "r") as file:
        data = json.load(file)
        send_notification(data.get("message", "No message"))
    time.sleep(10)
