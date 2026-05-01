import telebot 
from telebot.types import InlineKeyboardButton , InlineKeyboardMarkup
from telebot.types import ReplyKeyboardMarkup

bot = telebot.TeleBot('7275915181:AAFP7rBPJ_GtTvBf8CqvPgxnPWl-OfSLQVI')

button1 = InlineKeyboardButton("First")
button2 = InlineKeyboardButton("Second")

inline_keyboard = InlineKeyboardMarkup(row_width=1)
inline_keyboard.add(button1 , button2)

