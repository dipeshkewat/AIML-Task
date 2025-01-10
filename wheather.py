import requests

def get_weather(city):
    api_key = "d1bcd8d696de9b50a756bafcd0652c75"  
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)


    if response.status_code == 200:  
        data = response.json()  


        city_name = data["name"]
        temperature = data["main"]["temp"]
        weather_description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]


        print(f"Weather in {city_name}:")
        print(f"Temperature: {temperature}°C")
        print(f"Description: {weather_description.capitalize()}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print(f"Failed to get weather data. Error Code: {response.status_code}")

        

city = input("Enter city name: ")
get_weather(city)
