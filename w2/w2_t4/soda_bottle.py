class SodaBottle:
    def __init__(self, brand: str, volume: float) -> None:
        self.brand: str = brand
        self.volume: float = volume

    def __str__(self) -> str:
        return f"brand - {self.brand}\n  volume - {self.volume}"
