from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Agri Mitra Backend is Running 🚜"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_text = data.get("text", "")

    reply = f"Agri Mitra response to: {user_text}"

    return jsonify({
        "text": reply
    })

if __name__ == "__main__":
    app.run(debug=True)