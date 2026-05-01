import telebot 
from telebot.types import InlineKeyboardButton , InlineKeyboardMarkup
from telebot.types import ReplyKeyboardMarkup

bot = #Bot's API

button1 = InlineKeyboardButton(text="first one" , url= "https://google.com")
button2 = InlineKeyboardButton(text="second one" , callback_data="btn")

inline_keyboard = InlineKeyboardMarkup(row_width=1)
inline_keyboard.add(button1 , button2)


@bot.callback_query_handler(func=lambda call : True)
def check_btn(call) : 
    if call.data == "btn" : 
        bot.answer_callback_query(call.id , "btn is tapped" , show_alert= True)
    elif call.data == "https://google.com" : 
        bot.answer_callback_query(call.id , "googld is ok")


@bot.message_handler(commands=["start"])
def welcome(message) :
    bot.send_message(message.chat.id , "welcome to my first start of bot" , reply_markup = inline_keyboard) 
    bot.reply_to(message , "I'm too EXCITEDD!!!")
    bot.reply_to(message , "this is the keyboard" , reply_markup = reply_keyboard)

@bot.message_handler(content_types= ['document' , 'audio'])
def handle_docs_audio(message) : 
    if message.audio : 
        bot.reply_to(message , "nice sound")
    elif message.document : 
        bot.reply_to(message , "i'll check it")


@bot.message_handler(regexp= "amir")
def handle_message(message) : 
    bot.reply_to(message , "there he is!!")


@bot.message_handler(commands=["register"])
def send_a_message(message) : 
    bot.send_message(message.chat.id , "Enter the name : ")
    bot.register_next_step_handler(message , process_name)

def process_name(message) : 
    name = message.text
    bot.send_message(message.chat.id , f"you are {name}! How old are you ? ")

    bot.register_next_step_handler(message , age )

def age(message) : 
    person_age = message.text
    bot.send_message(message.chat.id , f"You are {person_age} ? good!")


reply_keyboard = ReplyKeyboardMarkup(resize_keyboard= True , one_time_keyboard= False)
reply_keyboard.add("button1" , "button2")


@bot.message_handler(func=lambda message : True)
def check_button(message) : 
    if message.text == 'button1':
        bot.reply_to(message , "b1 is pressed")
    elif message.text == 'button2':
        bot.reply_to(message , "b2 is pressed")


bot.polling()
