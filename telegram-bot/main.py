import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import *
import responses
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PKOB.settings')
django.setup()

API_KEY = "secret"

# Set up the logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot...')


def start_command(update, context):
    user = update.message.from_user.first_name
    update.message.reply_text('Hello {}! Saya ialah pkob_270607_bot. Bagaimana saya boleh membantu anda hari ini?'.format(user), reply_markup=start_menu_keyboard())


def main_menu(update, context):
    update.callback_query.message.edit_text("Sila pilih fungsi untuk meneruskan.",
                                            reply_markup=main_menu_keyboard())


def help_menu(update, context):
    update.callback_query.message.edit_text("Apa yang boleh saya bantu? Sila hubungi kami.",
                                            reply_markup=help_menu_keyboard())


def contact_menu(update, context):
    update.callback_query.message.edit_text("Nombor Telefon 0103373164\nEmail: yiqingtan99@gmail.com",
                                            reply_markup=contact_menu_keyboard())


def about_menu(update, context):
    update.callback_query.message.edit_text("Ketahui lebih lanjut tentang kami!",
                                            reply_markup=about_menu_keyboard())


def about_me_menu(update, context):
    update.callback_query.message.edit_text("PKOB adalah sistem berpusat dengan tujuan untuk membantu mangsa yang "
                                            "menghadapi masalah bencana untuk meminta bantuan. Saya pkob_270607_bot "
                                            "dan saya boleh membantu anda 24 jam untuk menyelesaikan rasa ingin tahu "
                                            "anda. Untuk mengetahui tentang kami, anda boleh melayari laman web kami.",
                                            reply_markup=aboutme_menu_keyboard())


def web_menu(update, context):
    update.callback_query.message.edit_text("https://pkob-270607.herokuapp.com/",
                                            reply_markup=website_menu_keyboard())


def get_data_menu(update, context):
    update.callback_query.message.edit_text("Sila beritahu saya Nombor Kad Pengenalan dan Nombor Telefon anda.\nContoh: 123456789456@0123456789",
                                            reply_markup=getinfo_keyboard())


def handle_message(update, context):
    text = str(update.message.text).lower()
    logging.info(f'User ({update.message.chat.id}) says: {text}')
    response = responses.get_response(text)

    # Bot response
    update.message.reply_text(response)


def handle_data(update, context):
    text = str(update.message.text).lower()
    if "@" in text:
        logging.info(f'User ({update.message.chat.id}) says: {text}')
        update.message.reply_text("Saya sedang cuba mencari maklumat, sila tunggu sebentar...")
        response = responses.get_data(text)
    else:
        response = responses.get_response(text)
    # Bot response
    update.message.reply_text(response)


def error(update, context):
    # Logs errors
    logging.error(f'Update {update} caused error {context.error}')


def start_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Mulakan Sekarang!', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)


def main_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton('Dapatkan maklumat', callback_data='getdata')],
        [InlineKeyboardButton('Pusat Bantuan', callback_data='help'),
         InlineKeyboardButton('Tentang Bot Ini', callback_data='about')]
    ]
    return InlineKeyboardMarkup(keyboard)


def getinfo_keyboard():
    keyboard = [
        [InlineKeyboardButton('Dapatkan maklumat', callback_data='getdata')],
        [InlineKeyboardButton('Pusat Bantuan', callback_data='help'),
         InlineKeyboardButton('Tentang Bot Ini', callback_data='about')]
    ]
    return InlineKeyboardMarkup(keyboard)


def help_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Hubungi Kami', callback_data='contactus')],
                [InlineKeyboardButton('Kembali ke menu utama', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)


def contact_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Kembali', callback_data='help')],
                [InlineKeyboardButton('Kembali ke menu utama', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)


def about_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Tentang Kami', callback_data='us'), InlineKeyboardButton('Laman Web', callback_data='web')],
                [InlineKeyboardButton('Kembali ke menu utama', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)


def aboutme_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Kembali', callback_data='about')],
                [InlineKeyboardButton('Kembali ke menu utama', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)


def website_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Kembali', callback_data='about')],
                [InlineKeyboardButton('Kembali ke menu utama', callback_data='main')]]
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
    dp.add_handler(CallbackQueryHandler(about_me_menu, pattern='us'))
    dp.add_handler(CallbackQueryHandler(web_menu, pattern='web'))
    dp.add_handler(CallbackQueryHandler(get_data_menu, pattern='getdata'))
    # dp.add_handler(CommandHandler('getdata', get_data_command))

    # Messages

    # dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_handler(MessageHandler(Filters.text, handle_data))

    # Log all errors
    dp.add_error_handler(error)

    # Run the bot
    updater.start_polling(1.0)
    updater.idle()
