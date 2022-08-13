#pip3 install torch
#pip install -U sacremoses
import os
import psutil #pip install psutil
import telebot #pip install pyTelegramBotAPI

import jsonpickle

from transformers import FSMTForConditionalGeneration, FSMTTokenizer
mname = "facebook/wmt19-en-ru"
tokenizer = FSMTTokenizer.from_pretrained(mname)
model = FSMTForConditionalGeneration.from_pretrained(mname)

token = 'Fill it'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Введите текст на английском')

@bot.message_handler(content_types=['text'])
def send_text(message):
    action_function(message)

def action_function(message):
    if message.text.lower():
        input = message.text
        input_ids = tokenizer.encode(input, return_tensors="pt")
        outputs = model.generate(input_ids)
        decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
        bot.send_message(message.chat.id, decoded)


bot.polling()
