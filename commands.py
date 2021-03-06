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

def hoy(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=sergas.get_new_cases_lastday(), parse_mode=ParseMode.HTML)

def total(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=sergas.get_total_cases_lastday(), parse_mode=ParseMode.HTML)

def dia(update, context):
    if (len(context.args) > 0):
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=sergas.get_total_cases_day(context.args[0]), parse_mode=ParseMode.HTML)
    else:
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=lang["dia-format"], parse_mode=ParseMode.HTML)

def help(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=lang["help"], parse_mode=ParseMode.HTML)

commands = {
    'start': CommandHandler('start', start),
    'dia': CommandHandler('dia', dia),
    'help': CommandHandler('help', help),
    'hoy': CommandHandler('hoy', hoy),
    'total': CommandHandler('total', total)
}
