from flask import Flask, jsonify
import threading
import time
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running! 🏁"

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": time.time(),
        "bot": "Anime group chat Bot",
        "service": "Active"
    })

@app.route('/ping')
def ping():
    return "pong", 200

def run():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

def keep_alive():
    t = threading.Thread(target=run)
    t.daemon = True
    t.start()
