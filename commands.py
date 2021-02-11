from telegram.ext import CommandHandler
from telegram import ParseMode
from sergas_info import Sergas
from lang_module import Lang

lang = Lang().get_lang_file()
sergas = Sergas()


def start(update, context):
    welcome = lang["welcome"]
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=welcome, parse_mode=ParseMode.HTML)


def covidtotal(update, context):
    chatid = update.effective_chat.id

    if (len(context.args) > 0 and context.args[0] == "dias"):
        context.bot.send_message(
            chat_id=chatid, text=sergas.get_total_cases_lastday(), parse_mode=ParseMode.HTML)
    elif (len(context.args) > 0 and context.args[0] == "ultimos"):
        context.bot.send_message(
            chat_id=chatid, text="Estamos trabajando en ello! Fdo. Aznar")
    else:
        context.bot.send_message(
            chat_id=chatid, text=lang["covidtotal-format"], parse_mode=ParseMode.HTML)
        return


def help(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=lang["help"], parse_mode=ParseMode.HTML)


commands = {
    'start': CommandHandler('start', start),
    'covidtotal': CommandHandler('covidtotal', covidtotal),
    'help': CommandHandler('help', help)
}
