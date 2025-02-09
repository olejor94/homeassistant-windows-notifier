from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/notify", methods=["POST"])
def notify():
    data = request.get_json()
    message = data.get("message", "No message received")

    # Send Windows-varsling via PowerShell
    os.system(f'powershell.exe -command "New-BurntToastNotification -Text \\"{message}\\" "')

    return {"status": "Notification sent"}

if __name__ == "__main__":
    port = int(os.getenv("SERVER_PORT", 5000))
    app.run(host="0.0.0.0", port=port)
