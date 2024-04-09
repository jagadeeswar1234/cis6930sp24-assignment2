import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from assignment2 import calculate_location_ranks

def test_calculate_location_ranks():
    incidents = [
        ['04/03/2022 00:00', 'Event', 'LocationA', 'Nature1', ''],
        ['04/03/2022 01:00', 'Event', 'LocationB', 'Nature2', 'EMSSTAT'],
        ['04/03/2022 02:00', 'Event', 'LocationA', 'Nature1', '']
    ]
    expected_ranks = {'LocationA': 1, 'LocationB': 2}
    assert calculate_location_ranks(incidents) == expected_ranks
