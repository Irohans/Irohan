from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "こんにちは、Flask！"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render用にPORTを環境変数から取得
    app.run(host="0.0.0.0", port=port)
