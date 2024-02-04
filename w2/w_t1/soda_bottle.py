class SodaBottle:
    def __init__(self, brand: str, volume: float) -> None:
        self.brand: str = brand
        self.volume: float = volume

    def serialize(self) -> str:
        return f"{self.brand};{self.volume}"