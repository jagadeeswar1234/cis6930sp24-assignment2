

from assignment2 import check_emsstat

def test_check_emsstat():
    incidents = [
        ['04/03/2022 00:00', 'Event', 'LocationA', 'Nature1', 'EMSSTAT'],
        ['04/03/2022 01:00', 'Event', 'LocationB', 'Nature2', '']
    ]
    assert check_emsstat(incidents[0], incidents, 0) == True
    assert check_emsstat(incidents[1], incidents, 1) == False
