from soda_bottle import SodaBottle

class Main:
    def __init__(self) -> None:
        print("Program starting.")
        self.run()
        print("Program ending.")
        return None

    def run(self) -> None:
        filename: str = input("Insert filename: ")
        with open(filename, 'r') as file:
            first_row: str = file.readline().strip()
            print(f'Deserializing "{first_row}"')
            soda_bottle: SodaBottle = SodaBottle.deserialize(first_row)
            print(f"Looks like {soda_bottle.volume} litre {soda_bottle.brand} bottle.")
        return None

if __name__ == "__main__":
    app: Main = Main()
