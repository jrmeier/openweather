import requests


class OpenWeatherApi(object):
    
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'http://api.openweathermap.org/data/2.5/weather'
    
    def get_weather_by_city(self, city_input):
        formatted_city = self.format_string(city_input)

        if not formatted_city:
            return 'City could not be parsed from string: {0}'.format(city_input)
        params = {'appid': self.api_key, 'q':formatted_city,'units':'imperial'}
        req = requests.get(self.base_url, params=params)
        if req.status_code not in range(200, 206):
            return 'Weather not found for: {0}'.format(formatted_city)
            
        return '{0} degrees Fahrenheit'.format(req.json()['main']['temp'])
    

    def format_string(self, city_input):
        url = 'http://maps.googleapis.com/maps/api/geocode/json'
        params = {'address': city_input}
        response = requests.get(url, params=params)
        if response.status_code not in range(200, 206):
            return None
        try:
            response = response.json()

            city_string = response['results'][0]['formatted_address'].split(',')
        except IndexError:
            return None
        
        return city_string[0]+ ','+city_string[2]
