from telegram.ext import CommandHandler
from sergas_info import Sergas

sergas = Sergas()


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="TEST")


def covid(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=sergas.get_total_cases("2021-02-08"))


commands = {
    'start': CommandHandler('start', start),
    'covid': CommandHandler('covid', covid)
}
