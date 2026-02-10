from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Secure DevSecOps Demo Running!"

@app.route("/secret")
def secret():
    return os.getenv("APP_SECRET", "No secret found!")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
