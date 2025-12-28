from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/name")
def home():
    return "Hello, this is Ajay"

@app.route("/number")
def health():
    return "7729033826"

    app.run(host="0.0.0.0", port=5000)
