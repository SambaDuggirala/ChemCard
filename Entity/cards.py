class Card:
    """Base class for all the cards to derive from"""

    def __init__(self, name: str = "Primitive card", type: str = "Primitive"):
        self.name = name
        self.type = type
