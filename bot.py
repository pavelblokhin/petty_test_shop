import telebot
import webbrowser

bot = telebot.TeleBot('6955234379:AAEcszwsZNB9QfOqa_oxk_gnO-F2HWaS1WY')

@bot.message_handler(comands=['site', 'website'])
def site(message):
    webbrowser.open('https://www.youtube.com/watch?v=ObwoMskHDoA&list=PL0lO_mIqDDFUev1gp9yEwmwcy8SicqKbt')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Hi, lets start test')
    
@bot.message_handler(commands='help')
def helpim(message):
    bot.send_message(message.chat.id, f"Hello, {message.from_user.first_name}, I'll help you")
    
@bot.message_handler()
def info(message):
    if message.text.lower() == 'Hello':
        bot.send_message(message.chat.id, f"Hello, {message.from_user.first_name}")
    elif 'id' in message.text.lower():
        bot.reply_to(message, f'ID: {message.from_user.id}')
        
    
    
bot.polling(non_stop=True)