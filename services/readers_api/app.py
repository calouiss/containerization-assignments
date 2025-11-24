from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/readers", methods=["GET"])
def get_readers():
    return jsonify({
        "data": ["cynthia", "ann", "louis"],
        "service": "readers-api"
    }), 200

@app.route("/health")
def health():
    return "healthy", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
