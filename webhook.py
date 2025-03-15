from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

# Route để xác thực Zalo domain
@app.route('/<filename>')
def verify_domain(filename):
    return send_from_directory(os.getcwd(), filename)

@app.route("/", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        return "Zalo Webhook Active!", 200
    elif request.method == "POST":
        data = request.json
        print("📩 Received Webhook:", data)
        return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(port=5000, debug=True)
