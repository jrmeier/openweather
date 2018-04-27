import unittest
from tests import test_open_weather_api
from open_weather_api import OpenWeatherApi


def suite():
    return unittest.TestSuite([
        test_open_weather_api.suite()
    ])