from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Replace 'YOUR_BOT_TOKEN' with your actual Telegram bot token
bot_token = '7402615050:AAGe47Qi9Zls2kpyujYG3OV7oJruJiuY-DY'
bot = Bot(token=bot_token)

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hello! I'm your simple Telegram chatbot. How can I help you today?")

def echo(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    update.message.reply_text(f"You said: {user_message}")

def main():
    updater = Updater(token=bot_token, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
