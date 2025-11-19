from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({"status": "healthy", "service": "readers-api"})

@app.route("/api/readers")
def readers_root():
    return jsonify({"service": "readers-api", "data": ["r1", "r2", "r3"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)