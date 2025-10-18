from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>✅ Flask Server Works on port 8000!</h1>"

if __name__ == "__main__":
    # از پورت 8000 استفاده می‌کنیم که احتمالاً آزاد است
    app.run(host="0.0.0.0", port=8000, debug=True)
