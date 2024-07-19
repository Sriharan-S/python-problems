import requests

def get_weather(city, api_key):
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        print(f"Current weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Weather: {weather}")
    else:
        print(f"Failed to get weather data for {city}. HTTP Status code: {response.status_code}")

api_key = 'API_HIDDEN_LOL'
city = input("Enter the city name: ")
get_weather(city, api_key)
