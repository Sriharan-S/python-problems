from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging

logging.basicConfig(filename='chat_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hello! I am your bot. Send me a message and I will log it.')

def log_message(update: Update, context: CallbackContext) -> None:
    """Log incoming messages to a file."""
    user = update.message.from_user.username or update.message.from_user.id
    text = update.message.text
    logging.info(f"User: {user}, Message: {text}")
    update.message.reply_text(f"Message logged: {text}")

def main() -> None:
    """Start the bot."""
    updater = Updater("bot token")
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, log_message))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
