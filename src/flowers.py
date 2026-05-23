from pydantic import BaseModel


class Tulip(BaseModel):
    """
    Represents a tulip flower sold by the flower shop.

    Attributes:
        variety (str):
            Commercial or botanical variety name of the tulip.

        color (str):
            Primary flower color.

        stem_length_cm (int):
            Stem length in centimeters.

        price (float):
            Retail price per tulip in EUR.
    """

    variety: str
    color: str
    stem_length_cm: int
    price: float

    def description(self) -> str:
        """
        Generate a human-readable tulip description.

        Returns:
            str:
                Formatted tulip description including color,
                variety name, and stem length.
        """

        return (
            f"{self.color} {self.variety} tulip "
            f"({self.stem_length_cm} cm)"
        )
