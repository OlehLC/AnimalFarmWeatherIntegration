import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import requests
import telebot
from src.utils.config import OPENWEATHER_API_KEY, CITY, TELEGRAM_TOKEN, CHAT_ID

# Виклик API
url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={OPENWEATHER_API_KEY}&units=metric"
response = requests.get(url)
weather_data = response.json()
temperature = weather_data['main']['temp']

# Відправка повідомлення в чат, якщо температура < -5°C
bot = telebot.TeleBot(TELEGRAM_TOKEN)
if temperature > -5:
    message = f"Увага! Температура в {CITY} становить {temperature}°C. Все добре !!"
    bot.send_message(CHAT_ID, message)
    print("Повідомлення відправлено в чат!")
else:
    print("Температура в межах норми.")