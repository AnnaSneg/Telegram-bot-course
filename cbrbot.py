"""
Telegram bot.
The bot outputs the exchange rate of the Central Bank of the selected currency for today or returns a chart of exchange
rate fluctuations for the period. 
"""
from telegram.ext import Updater, CommandHandler

from cbr_daily import course_val
import traceback
import datetime
import plot

APITOKEN = "..." # use your own APITOKEN
updater = Updater(token=APITOKEN)
dispatcher = updater.dispatcher


def get_chat_id(u):
    m = u.message if u.message != None else u.edited_message
    return m.chat_id


def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="Hello! I'm a bot! Do you want to know today's courses or the course for the period? "
                                  "Enter '/course CURRENCY' or '/course CURRENCY date_start = yyyy-mm-dd date_end = "
                                  "yyyy-mm-dd")
    print("/start command, user:", update.effective_user.link)


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


def course(update, context):
    try:
        print("/course command, user:", update.effective_user.username, update.effective_user.link, "args = ",
              context.args)
        if len(context.args) == 0:
            context.bot.send_message(update.message.chat_id, "missing argument: CCY")
            return
        ccy = context.args[0].upper()
        if len(context.args) == 1:
            context.bot.send_message(chat_id=update.message.chat_id, text=course_val(ccy))
            return
        if len(context.args) != 3:
            context.bot.send_message(update.message.chat_id, "expected: /course <CCY> <date_start> <date_end>")
            return
        try:
            date_start = datetime.datetime.strptime(context.args[1], '%Y-%m-%d')
        except:
            context.bot.send_message(update.message.chat_id, "expected: date in yyyy-mm-dd format")
            return
        try:
            date_end = datetime.datetime.strptime(context.args[2], '%Y-%m-%d')
        except:
            context.bot.send_message(get_chat_id(update), "expected: date in yyyy-mm-dd format")
            return
        context.bot.send_photo(get_chat_id(update), plot.get_picture(ccy, date_start, date_end))
    except:
        traceback.print_exc()
        raise


course_handler = CommandHandler('course', course)
dispatcher.add_handler(course_handler)

print("BEFORE START POLLING...")
updater.start_polling()
