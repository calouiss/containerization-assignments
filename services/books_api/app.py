from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/books", methods=["GET"])
def get_books():
    return jsonify({
        "data": ["1984", "Dune", "Foundation"],
        "service": "books-api"
    }), 200

@app.route("/health")
def health():
    return "healthy", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
