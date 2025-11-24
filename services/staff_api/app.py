from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/staff", methods=["GET"])
def get_staff():
    return jsonify({
        "data": ["cynthia", "ann", "louis"],
        "service": "staff-api"
    }), 200

@app.route("/health")
def health():
    return "healthy", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
