from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/notify', methods=['POST'])
def notify():
    data = request.json
    title = data.get('title', 'Home Assistant')
    message = data.get('message', 'No message provided')

    print(f"Notification received: {title} - {message}")
    
    return jsonify({"status": "sent"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
