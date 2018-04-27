from open_weather_api import OpenWeatherApi
appid = ''

def check_weather():
    api = OpenWeatherApi(appid)
    city_string = input('What city are you in? ')
    print(api.get_weather_by_city(city_string))

if __name__ == '__main__':
    check_weather()