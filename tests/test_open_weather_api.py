import unittest
import mock
from open_weather_api import OpenWeatherApi
#from helpers import format_string
import json


class TestOpenWeatherApi(unittest.TestCase):
    """
    Test cases for the openweather Api
    """
    def mock_response(self, status=200, content="CONTENT", json_data=None,raise_for_status=None):
        mock_resp = mock.Mock()
        # mock raise_for_status call w/optional error
        mock_resp.raise_for_status = mock.Mock()
        if raise_for_status:
            mock_resp.raise_for_status.side_effect = raise_for_status
        # set status code and content
        mock_resp.status_code = status
        mock_resp.content = content
        # add json data if provided
        if json_data:
            mock_resp.json = mock.Mock(
                return_value=json_data
            )
        return mock_resp

    @mock.patch('open_weather_api.requests.get')
    def test_format_string_case1(self, mock_get):
        api = OpenWeatherApi("appid")
        city_input = "Chicago,il"
        json_data = {
            'results':[
                {'formatted_address':'Chicago, IL, USA'}
            ]
        }

        mock_get.return_value = self.mock_response(json_data=json_data)
        result = api.format_string(city_input)
        self.assertEqual(result, "Chicago, USA")
    
    @mock.patch('open_weather_api.requests.get')
    def test_format_string_case2(self, mock_get):
        api = OpenWeatherApi("appid")
        city_input = "Chicago,il"
        json_data = {
            'results':[
                {'formatted_address':'Des Moines, IA, USA'}
            ]
        }

        mock_get.return_value = self.mock_response(json_data=json_data)
        result = api.format_string(city_input)
        self.assertNotEqual(result, "Chicago, USA")
    
    def test_get_weather_by_city(self):
        api = OpenWeatherApi("appid")
        self.assertIsInstance(api, OpenWeatherApi)



    


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestOpenWeatherApi)


if __name__ == "__main__":
    unittest.main()
    #unittest.TextTestRunner(verbosity=2).run(suite())