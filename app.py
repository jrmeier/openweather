from open_weather_api import OpenWeatherApi
api_key = "523c2f66a7b20a05595560808f5f12b3"

def check_weather():
    api = OpenWeatherApi(api_key)
    city_string = input("What city are you in? ")
    print(api.get_weather_by_city(city_string))

if __name__ == '__main__':
    check_weather()