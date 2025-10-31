from flask import Flask, request, jsonify

app = Flask(__name__)

@app.get("/health")
def health():
    return jsonify(status="ok"), 200

@app.get("/GET")
def get_endpoint():
    return jsonify(message="Hello from the container!", client=request.remote_addr), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
