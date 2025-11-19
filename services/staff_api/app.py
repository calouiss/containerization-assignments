from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({"status": "healthy", "service": "staff-api"})

@app.route("/api/staff")
def staff_root():
    return jsonify({"service": "staff-api", "data": ["cynthia", "ann", "louis"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)