from telegram.ext import CommandHandler
from telegram import ParseMode
from sergas_info import Sergas
import json

with open("lang.json", "r") as file:
    lang = json.loads(file.read())

sergas = Sergas()


def start(update, context):
    welcome = lang["welcome"]
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=welcome, parse_mode=ParseMode.HTML)


def covidtotal(update, context):
    chatid = update.effective_chat.id

    if (len(context.args) > 0 and context.args[0] == "dias"):
        context.bot.send_message(
            chat_id=chatid, text=sergas.get_total_cases("2021-02-08"))
    elif (len(context.args) > 0 and context.args[0] == "ultimos"):
        context.bot.send_message(
            chat_id=chatid, text=sergas.get_last_ten_days())
    else:
        context.bot.send_message(
            chat_id=chatid, text=lang["covidtotal-format"], parse_mode=ParseMode.HTML)
        return


commands = {
    'start': CommandHandler('start', start),
    'covidtotal': CommandHandler('covidtotal', covidtotal)
}
