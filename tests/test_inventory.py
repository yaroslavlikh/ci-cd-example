import pytest

from src.flowers import Tulip
from src.inventory import Inventory


def test_add_tulips():
    inventory = Inventory()

    tulip = Tulip(
        variety="Queen of Night",
        color="Purple",
        stem_length_cm=40,
        price=3.5,
    )

    inventory.add_tulip(tulip, quantity=5)

    assert inventory.count("Queen of Night") == 5


def test_remove_tulips():
    inventory = Inventory()

    tulip = Tulip(
        variety="Angelique",
        color="Pink",
        stem_length_cm=35,
        price=4.0,
    )

    inventory.add_tulip(tulip, quantity=3)
    inventory.remove_tulip("Angelique", quantity=2)

    assert inventory.count("Angelique") == 1


def test_remove_too_many_tulips():
    inventory = Inventory()

    with pytest.raises(ValueError):
        inventory.remove_tulip("Nonexistent", quantity=1)