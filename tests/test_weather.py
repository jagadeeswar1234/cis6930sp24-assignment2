
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from assignment2 import weather_code

def test_weather_code():
    # Test the weather_code function's ability to return an integer
    api_key = 'dummy_api_key'
    date_time_str = '2022-04-04 12:00'
    result = weather_code(api_key, date_time_str)
    assert isinstance(result, int)