import sqlite3
import config
from telebot import TeleBot
from telebot.types import KeyboardButton , ReplyKeyboardMarkup

def create_table() : 
    connection = sqlite3.connect("bot_users.db")
    cursor = connection.cursor()
    query = """
    CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        phone_number VARCHAR(255),
        user_id VARCHAR(255)
    );"""

    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()

create_table()


def insert() : 
    connection = sqlite3.connect("bot_users.db")
    cursor = connection.cursor()
    query = """INSERT INTO Users(name , password) VALUES ('amirreza','1234')"""
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()

#the bot
bot = TeleBot("7275915181:AAFP7rBPJ_GtTvBf8CqvPgxnPWl-OfSLQVI")
#keyboard
keyboard = ReplyKeyboardMarkup(resize_keyboard= True , row_width= 1)
button = KeyboardButton(text= "send info" , request_contact= True)

keyboard.add(button)

#the data_base

@bot.message_handler(commands=['start'])
def welcome(message) : 
    bot.send_message(message.chat.id , text= "hello there weolcome again" , reply_markup=keyboard)


@bot.message_handler(content_types= ['contact'])
def contact(message) : 
    # bot.send_message(message.chat.id , text=f'{message.contact}')
    connection = sqlite3.connect("bot_users.db")
    cursor = connection.cursor()
    insert_query = f"""INSERT INTO Users (phone_number , user_id) VALUES ('{message.contact.phone_number}' , '{message.contact.user_id}' )"""
    cursor.execute(insert_query)
    connection.commit()
    


bot.polling()   