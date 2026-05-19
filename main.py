from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from fyers_apiv3 import fyersModel
import os

BOT_TOKEN = os.getenv("TOKEN")
FYERS_APP_ID = os.getenv("FYERS_APP_ID")
FYERS_SECRET_KEY = os.getenv("FYERS_SECRET_KEY")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Trading bot online 🚀")

async def login(update: Update, context: ContextTypes.DEFAULT_TYPE):

    session = fyersModel.SessionModel(
        client_id=FYERS_APP_ID,
        secret_key=FYERS_SECRET_KEY,
        redirect_uri="https://google.com",
        response_type="code",
        grant_type="authorization_code"
    )

    auth_url = session.generate_authcode()

    await update.message.reply_text(
        f"Login to FYERS:\n{auth_url}"
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("login", login))

print("Trading bot started...")

app.run_polling()
