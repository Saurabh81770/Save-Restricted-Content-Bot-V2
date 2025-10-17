import threading
from flask import Flask
from pyrogram import Client

API_ID = int("your_api_id")
API_HASH = "your_api_hash"
BOT_TOKEN = "your_bot_token"

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running fine!"

def run_web():
    app.run(host="0.0.0.0", port=8080)

def run_bot():
    bot = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
    bot.run()

if __name__ == "__main__":
    threading.Thread(target=run_web).start()
    run_bot()
