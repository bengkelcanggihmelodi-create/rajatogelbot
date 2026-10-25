import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_IDS = [int(x) for x in os.getenv("ADMIN_IDS","").split(",") if x.strip().isdigit()]

LOGIN_URL = "https://super.rajatogelidr.com/login"
REGISTER_URL = "https://super.rajatogelidr.com/register"

async def start(update, context: ContextTypes.DEFAULT_TYPE):
    kb = [[InlineKeyboardButton("🔐 LOGIN", url=LOGIN_URL), InlineKeyboardButton("📝 REGISTER", url=REGISTER_URL)]]
    await update.message.reply_text("👋 Selamat datang di RAJATOGEL Support Bot\nKlik LOGIN untuk masuk:", reply_markup=InlineKeyboardMarkup(kb))

async def acc(update, context):
    if update.effective_user.id not in ADMIN_IDS: return
    await context.bot.send_message(int(context.args[0]), f"✅ Deposit di-ACC! Login: {LOGIN_URL}")
    await update.message.reply_text("ACC OK")

async def tolak(update, context):
    if update.effective_user.id not in ADMIN_IDS: return
    await context.bot.send_message(int(context.args[0]), f"❌ DITOLAK")
    await update.message.reply_text("TOLAK OK")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("acc", acc))
    app.add_handler(CommandHandler("tolak", tolak))
    app.run_polling()

if __name__ == "__main__":
    main()
