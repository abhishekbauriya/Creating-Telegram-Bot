import logging 
from telegram import Bot, Update
from telegram.ext import Updater, Filters, CallbackContext, CommandHandler, MessageHandler, Dispatcher
from flask import Flask, request

#Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s -%(message)s',
	                level=logging.INFO)

logger = logging.getLogger(__name__)

TOKEN = "1631055822:AAER3YEoFPVwlim5N5b1HEhI94QXPWAd83Q"

app = Flask(__name__)

@app.route('/')
def index():
	return "Hello!"

@app.route(f'/{TOKEN}', methods=['GET', 'POST'])
def webhook():
    """webhook view which receives updates from telegram"""
    # Create update object from json-format request data
    update = Update.de_json(request.get_json(), bot)
    # process update
    dp.process_update(update)
    return "ok"

def start(bot, update, context: CallbackContext):
	author = update.message.from_user.first_name
	reply = "Hi! {}".format(author)
	bot.send_message(chat_id=update.message.chat_id, text=reply)

def _help(bot, update, context: CallbackContext):
	help_text = "Hey! This is a help text."
	bot.send_message(chat_id=update.message.chat_id, text=help_text)

def echo_text(bot, update, context: CallbackContext):
	reply = update.message.text
	bot.send_message(chat_id=update.message.chat_id, text=reply)

def echo_sticker(bot, update, context: CallbackContext):
	bot.send_sticker(chat_id=update.message.chat_id, sticker=update.message.sticker.file_id)

def error(bot, update, context: CallbackContext):
	logger.error("Update '%s' caused error '%s'", update, update.error)

def message_handler(update, context: CallbackContext):
 	update.message.reply_text(text)

if __name__ == "__main__":
	bot = Bot(TOKEN)
	bot.set_webhook("https://48c9acd55480.ngrok.io/" + TOKEN)

	dp = Dispatcher(bot, None)
	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(CommandHandler("help", _help))
	dp.add_handler(MessageHandler(Filters.text, echo_text))
	dp.add_handler(MessageHandler(Filters.sticker, echo_sticker))
	dp.add_error_handler(error)
	app.run(port=8443)