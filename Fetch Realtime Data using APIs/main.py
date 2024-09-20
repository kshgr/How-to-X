import requests

def fetch_weather_data(api_key, city, units='metric'):
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    complete_url = f"{base_url}appid={api_key}&q={city}&units={units}"
    response = requests.get(complete_url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code}")
        return None

if __name__ == "__main__":
    api_key = "<your_api_key>"
    city = input("Enter the city name: ")
    
    weather_data = fetch_weather_data(api_key, city)
    
    if weather_data:
        main = weather_data['main']
        temperature = main['temp']
        pressure = main['pressure']
        humidity = main['humidity']
        
        weather = weather_data['weather']
        weather_description = weather[0]['description']
        
        print(f"Temperature: {temperature}°C")
        print(f"Pressure: {pressure} hPa")
        print(f"Humidity: {humidity}%")
        print(f"Weather description: {weather_description}")
    else:
        print("Weather data not found.")
