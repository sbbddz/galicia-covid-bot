from telegram.ext import Updater
import commands as cmd

with open('token.txt', 'r') as token_file:
    token = token_file.read().strip()

updater = Updater(token=token, use_context=True)

for name, handler in cmd.commands.items():
    updater.dispatcher.add_handler(handler)
    print("Registered command: " + name)

updater.start_polling()
