import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import *
import responses
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PKOB.settings')
django.setup()

API_KEY = "5034966448:AAH11XjVKeSK9dIQr6pXGDCAlB5vSwswxdY"

# Set up the logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot...')


def start_command(update, context):
    update.message.reply_text('Hello there! I am PKOB Bot. How can I help you?', reply_markup=start_menu_keyboard())


def main_menu(update, context):
    update.callback_query.message.edit_text("Please choose a function to proceed.",
                                            reply_markup=main_menu_keyboard())


def help_menu(update, context):
    update.callback_query.message.edit_text("What can I help you? Please do not hesitate to contact us.",
                                            reply_markup=help_menu_keyboard())


def contact_menu(update, context):
    update.callback_query.message.edit_text("Contact Number: 0103373164\nEmail: yiqingtan99@gmail.com",
                                            reply_markup=contact_menu_keyboard())


def about_menu(update, context):
    update.callback_query.message.edit_text("Find out more about me!",
                                            reply_markup=about_menu_keyboard())


def about_me_menu(update, context):
    update.callback_query.message.edit_text("https://pkob-270607.herokuapp.com/",
                                            reply_markup=aboutme_menu_keyboard())


def web_menu(update, context):
    update.callback_query.message.edit_text("https://pkob-270607.herokuapp.com/",
                                            reply_markup=website_menu_keyboard())


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
    keyboard = [
        [InlineKeyboardButton('Get Info', callback_data='getdata')],
        [InlineKeyboardButton('Help', callback_data='help'),
         InlineKeyboardButton('About This Bot', callback_data='about')]
    ]
    return InlineKeyboardMarkup(keyboard)


def getinfo_keyboard():
    keyboard = [InlineKeyboardButton('Back', callback_data='main')]
    return InlineKeyboardMarkup(keyboard)


def help_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Contact Us', callback_data='contactus')],
                [InlineKeyboardButton('Back to main menu', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)


def contact_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Back to previous', callback_data='help')],
                [InlineKeyboardButton('Back to main menu', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)


def about_menu_keyboard():
    keyboard = [[InlineKeyboardButton('About Us', callback_data='aboutus'), InlineKeyboardButton('Our Website', callback_data='web')],
                [InlineKeyboardButton('Back to main menu', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)


def aboutme_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Back to previous', callback_data='about')],
                [InlineKeyboardButton('Back to main menu', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)


def website_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Back to previous', callback_data='about')],
                [InlineKeyboardButton('Back to main menu', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)


if __name__ == '__main__':
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher

    # Command
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CallbackQueryHandler(main_menu, pattern='main'))
    dp.add_handler(CallbackQueryHandler(help_menu, pattern='help'))
    dp.add_handler(CallbackQueryHandler(contact_menu, pattern='contactus'))
    dp.add_handler(CallbackQueryHandler(about_menu, pattern='about'))
    dp.add_handler(CallbackQueryHandler(about_me_menu, pattern='aboutus'))
    dp.add_handler(CallbackQueryHandler(web_menu, pattern='web'))
    dp.add_handler(CommandHandler('getdata', get_data_command))

    # Messages

    # dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_handler(MessageHandler(Filters.text, handle_data))

    # Log all errors
    dp.add_error_handler(error)

    # Run the bot
    updater.start_polling(1.0)
    updater.idle()
