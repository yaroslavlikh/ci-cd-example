from src.inventory import Inventory


class Order:
    def __init__(self, inventory: Inventory):
        self.inventory = inventory
        self.items = {}

    def add_item(self, variety: str, quantity: int):
        if self.inventory.count(variety) < quantity:
            raise ValueError("Insufficient stock")

        self.items[variety] = self.items.get(variety, 0) + quantity

    def total_price(self) -> float:
        total = 0.0

        for variety, quantity in self.items.items():
            tulips = self.inventory.stock[variety]

            if not tulips:
                continue

            unit_price = tulips[0].price
            total += unit_price * quantity

        return round(total, 2)

    def checkout(self):
        for variety, quantity in self.items.items():
            self.inventory.remove_tulip(variety, quantity)

        return {
            "status": "success",
            "items": self.items,
            "total": self.total_price(),
        }