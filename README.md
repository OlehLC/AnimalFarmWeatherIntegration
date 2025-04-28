 Інтеграція OpenWeather API для обліку тваринництва

 Опис сценарію використання
Цей проєкт інтегрує OpenWeather API для отримання погодних даних у систему обліку тваринництва.  
 Мета: Отримувати погодні дані (температура, вологість) для регіону ферми.  
 Сценарій:  
  1. Система періодично звертається до OpenWeather API для отримання поточної температури.  
  2. Якщо температура нижче 5°C, формується повідомлення для працівників ферми.  
  3. Повідомлення надсилається в корпоративний чат для попередження про можливі ризики падежу тварин.  

 API
 Сервіс: OpenWeather API (https://openweathermap.org/api)  
 Ендпоінт: `https://api.openweathermap.org/data/2.5/weather`  
 Параметри:  
   `q` — назва міста (наприклад, Kyiv).  
   `appid` — APIключ.  
   `units` — одиниці вимірювання (metric для °C).  
 Приклад запиту:  
 GET https://api.openweathermap.org/data/2.5/weather?q=Kyiv&appid=YOUR_API_KEY&units=metric
Приклад відповіді:  
```json
{
  "main": {
    "temp": 3.5,
    "humidity": 82
  },
  "weather": [
    {
      "description": "clear sky"
    }
  ]
}