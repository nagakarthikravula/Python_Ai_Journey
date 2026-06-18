import requests
from dotenv import load_dotenv
import os
def get_weather(city):
    try:
        url = f"https://wttr.in/{city}?format=j1"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to get weather data.")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def display_weather(data, city):
    current = data["current_condition"][0]
    condition = current["weatherDesc"][0]["value"]
    temp = current["temp_C"]
    feels_like = current["FeelsLikeC"]
    humidity = current["humidity"]
    wind_speed = current["windspeedKmph"]
    wind_dir = current["winddir16Point"]
    print(f'''
========================================
  Weather Report: {city}
========================================
  Condition   : {condition}
  Temperature : {temp}°C (Feels like {feels_like}°C)
  Humidity    : {humidity}%
  Wind Speed  : {wind_speed} km/h ({wind_dir})
========================================
''')


def main():
    load_dotenv()
    while True:
        city = input("Enter City Name: ")
        if city:
            data = get_weather(city)
            if data:
                display_weather(data, city)
                aip = input("Check another city? (yes/no): ")
                if aip.lower() == "no":
                    print("Goodbye!")
                    break

            else:
                print("Could not fetch weather. Please try again.")
        else:
            print("City name cannot be empty.")
        
if __name__ == "__main__":
    main()