from pathlib import Path 
import sys
root_dir = Path(__file__).parent.parent 
sys.path.insert(0, str(root_dir))
from src.flowers import Tulip


def test_tulip_description():
    tulip = Tulip(
        variety="Angelique",
        color="Pink",
        stem_length_cm=35,
        price=4.0,
    )

    assert tulip.description() == "Pink Angelique tulip (35 cm)"