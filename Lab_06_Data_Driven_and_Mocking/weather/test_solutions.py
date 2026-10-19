from unittest.mock import patch # in this case can control
from weather import describe_weather  #  CORRECT

def test_freezing_weather():
    with patch("weather.get_temperature", return_value = -5):
        assert describe_weather() == "Freezing"

def test_cold_weather():    
    with patch("weather.get_temperature", return_value=8):
        assert describe_weather() == "Cold"

def test_pleasant_weather():
    
    with patch("weather.get_temperature", return_value=20):
        assert describe_weather() == "Pleasant"
        
def test_hot_weather():
    with patch("weather.get_temperature" , return_value = 30):
        assert describe_weather() =="Hot"


