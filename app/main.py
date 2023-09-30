import telebot
import os 
import openai 
from dotenv import load_dotenv


load_dotenv()

openai.api_key = os.getenv("OPENAI_API_TOKEN")
bot = telebot.TeleBot(os.getenv("TELEGRAM_BOT_TOKEN"))

@bot.message_handler(content_types=['text'])
def handle_text(message):
    # Process text messages here
    bot.send_message(message.chat.id, "You sent a text message.")

@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    file_info = bot.get_file(message.voice.file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    with open("voice.ogg", 'wb') as new_file:
        new_file.write(downloaded_file)
    
    response = openai.Audio.transcribe(file=open("voice.ogg", 'rb'), model='whisper-1')

    bot.send_message(message.chat.id, response.text)

bot.polling()