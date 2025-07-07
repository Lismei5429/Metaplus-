import telebot

TOKEN = '7771234555:AAHiQY8MtKVxu30VuQdxbNwmyna6E1UnET8'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 ¡Bienvenido a Metaplus!\nEste es tu bot de minería. Pronto podrás comenzar a ganar.")

bot.infinity_polling()
