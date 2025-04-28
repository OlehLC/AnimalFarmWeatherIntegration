import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import matplotlib.pyplot as plt
import matplotlib
from src.api.weather_api import get_weather_data

# Налаштування шрифту для кирилиці
matplotlib.rc('font', family='DejaVu Sans')

def visualize_weather():
    weather_data = get_weather_data()
    if not weather_data:
        return None, None

    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    description = weather_data['weather'][0]['description']

    print(f"Погода в місті {weather_data['name']}:")
    print(f"Температура: {temperature}°C")
    print(f"Вологість: {humidity}%")
    print(f"Опис: {description}")

    # Візуалізація
    labels = ['Температура (°C)', 'Вологість (%)']
    values = [temperature, humidity]

    plt.figure(figsize=(6, 4))
    plt.bar(labels, values, color=['blue', 'green'])
    plt.title(f'Погодні дані для {weather_data["name"]}')
    plt.ylabel('Значення')
    plt.grid(True)
    plt.show()

    return temperature, humidity

if __name__ == "__main__":
    temperature, humidity = visualize_weather()
    if temperature is not None and temperature < -5:
        print(f"Увага! Температура становить {temperature}°C. Можливі ризики для тварин!")
    elif temperature is not None:
        print("Температура в межах норми.")