import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from assignment2 import calculate_incident_ranks

def test_calculate_incident_ranks():
    incidents = [
        ['04/03/2022 00:00', 'Event', 'LocationA', 'Nature1', ''],
        ['04/03/2022 01:00', 'Event', 'LocationB', 'Nature2', 'EMSSTAT'],
        ['04/03/2022 02:00', 'Event', 'LocationA', 'Nature1', '']
    ]
    expected_ranks = {'Nature1': 1, 'Nature2': 2}
    assert calculate_incident_ranks(incidents) == expected_ranks
