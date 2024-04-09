import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from assignment2 import determine_side_of_town

def test_determine_side_of_town():
    bearing = 90  # East
    assert determine_side_of_town(bearing) == "E"
