import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from assignment2 import get_day_of_week

def test_get_day_of_week():
    assert get_day_of_week("04/03/2022 00:00") == 1