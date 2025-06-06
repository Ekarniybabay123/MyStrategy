import pip
pip.main(['install', 'python-telegram-bot'])

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# === Настройки ===
TOKEN = '7912028611:AAFd5Be6Fd86TrGdST4lwiFzG6citKc1t9g'  # <-- Вставь свой токен

strategies = {
    "Пробой": "Норм уровень, проверь объем, посмотри на стакан, есть ли там активность и ликвидность",
    "Наклонка": "Наклонный уровень, проверь объем, посмотри на стакан, есть ли там активность и ликвидность, не трендовая ли это, трендовую аккуратно на истощении",
}

# === Команды ===

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[k] for k in strategies.keys()]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    await update.message.reply_text("Выбери стратегию:", reply_markup=reply_markup)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text in strategies:
        await update.message.reply_text(strategies[text])
    else:
        await update.message.reply_text("Не понимаю. Используй /start, чтобы выбрать стратегию.")

# === Основной запуск ===

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Бот запущен.")
    app.run_polling()

if __name__ == "__main__":
    main()
