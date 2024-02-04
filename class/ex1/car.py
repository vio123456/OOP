

class Car:
    color:str
    speed:float
    def __init__(self, color:str) -> None:
        self.color = color
        self.speed = 0.0
        pass
    def start(self) -> None:
        print(f"Car with color {self.color} started")
        return None
    def accelerate(self, amount:float) -> None:
        self.speed += 5.0
        return None