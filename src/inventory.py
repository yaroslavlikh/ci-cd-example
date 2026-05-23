from collections import defaultdict
from src.flowers import Tulip


class Inventory:
    def __init__(self):
        self.stock = defaultdict(list)

    def add_tulip(self, tulip: Tulip, quantity: int = 1):
        for _ in range(quantity):
            self.stock[tulip.variety].append(tulip)

    def count(self, variety: str) -> int:
        return len(self.stock[variety])

    def remove_tulip(self, variety: str, quantity: int = 1):
        if self.count(variety) < quantity:
            raise ValueError("Not enough tulips in stock")

        for _ in range(quantity):
            self.stock[variety].pop()

    def available_varieties(self):
        return [
            variety
            for variety, items in self.stock.items()
            if items
        ]