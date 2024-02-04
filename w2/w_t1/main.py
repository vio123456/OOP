from soda_bottle import SodaBottle

class Main:
    def __init__(self) -> None:
        print("Program starting.")
        self.run()
        print("Program ending.")
        return None

    def run(self) -> None:
        print("Constructing soda bottle.")
        brand: str = input("Insert brand: ")
        volume: float = float(input("Insert volume: "))
        
        soda_bottle: SodaBottle = SodaBottle(brand, volume)
        print("SodaBottle object created!\nSerializing SodaBottle object.")
        
        serialized_data: str = soda_bottle.serialize()
        print("Serialized sodabottle:\n" + serialized_data)
        return None

if __name__ == "__main__":
    app: Main = Main()