from src.flowers import Tulip
from src.inventory import Inventory
from src.order import Order


def create_sample_inventory() -> Inventory:
    inventory = Inventory()

    inventory.add_tulip(
        Tulip(
            variety="Queen of Night",
            color="Deep Purple",
            stem_length_cm=45,
            price=3.50,
        ),
        quantity=10,
    )

    inventory.add_tulip(
        Tulip(
            variety="Golden Apeldoorn",
            color="Yellow",
            stem_length_cm=40,
            price=2.75,
        ),
        quantity=15,
    )

    inventory.add_tulip(
        Tulip(
            variety="Angelique",
            color="Pink",
            stem_length_cm=38,
            price=4.25,
        ),
        quantity=8,
    )

    return inventory


if __name__ == "__main__":
    inventory = create_sample_inventory()

    order = Order(inventory)
    order.add_item("Queen of Night", 2)
    order.add_item("Angelique", 1)

    result = order.checkout()

    print("Order completed")
    print(result)