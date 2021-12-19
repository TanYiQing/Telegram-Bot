import logging
import time

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import *
import responses

API_KEY = "5034966448:AAH11XjVKeSK9dIQr6pXGDCAlB5vSwswxdY"

# Set up the logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot...')


def start_command(update, context):
    update.message.reply_text('Hello there! I am PKOB Bot. How can I help you?', reply_markup=start_menu_keyboard())


def main_menu(update, context):
    update.callback_query.message.edit_text("Please choose a function to proceed.", reply_markup=main_menu_keyboard())


def help_menu(update, context):
    update.callback_query.message.edit_text("What can I help you?", reply_markup=help_menu_keyboard())


def custom_command(update, context):
    update.message.reply_text("This is a custom command, you can add whatever text you want here.")


def handle_message(update, context):
    text = str(update.message.text).lower()
    logging.info(f'User ({update.message.chat.id}) says: {text}')
    response = responses.get_response(text)

    # Bot response
    update.message.reply_text(response)


def get_data_command(update, context):
    update.message.reply_text(
        "Please let me know your Nombor Kad Pengenalan and Nombor Telefon. For example 123456789456@0123456789")
    dp.add_handler(MessageHandler(Filters.text, handle_data))


def handle_data(update, context):
    text = str(update.message.text).lower()
    logging.info(f'User ({update.message.chat.id}) says: {text}')
    update.message.reply_text("I am trying to find the data, please wait a while...")
    response = responses.get_data(text)

    # Bot response
    update.message.reply_text(response)


def error(update, context):
    # Logs errors
    logging.error(f'Update {update} caused error {context.error}')


def start_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Get Start Now!', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)


def main_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Get Data', callback_data='getdata')],
                [InlineKeyboardButton('Help', callback_data='help')],
                [InlineKeyboardButton('About This Bot', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)


def help_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Contact Us', callback_data='getdata')],
                [InlineKeyboardButton('Feedback', callback_data='help')],
                [InlineKeyboardButton('Back', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)


if __name__ == '__main__':
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher

    # Command
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CallbackQueryHandler(main_menu, pattern='main'))
    dp.add_handler(CallbackQueryHandler(help_menu, pattern='help'))
    # dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('custom', custom_command))
    dp.add_handler(CommandHandler('getdata', get_data_command))

    # Messages
    # dp.add_handler(MessageHandler(Filters.text, handle_message))
    # dp.add_handler(MessageHandler(Filters.text, handle_data))

    # Log all errors
    dp.add_error_handler(error)

    # Run the bot
    updater.start_polling(1.0)
    updater.idle()
