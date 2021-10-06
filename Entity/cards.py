import arcade


class Card(arcade.Sprite):
    """Base class for all the cards to derive from"""

    def __init__(
        self,
        name: str = "Primitive card",
        type: str = "Primitive",
        sprite: str = "assets/primitive.png",
    ):
        self.name = name
        self.type = type
        super().__init__(f":resources:{sprite}")


print("This is a commit example.")
