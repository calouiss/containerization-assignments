from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({"status": "healthy", "service": "books-api"})

@app.route("/api/books")
def books_root():
    return jsonify({"service": "books-api", "data": ["1984", "Dune", "Foundation"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)