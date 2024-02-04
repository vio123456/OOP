from soda_bottle import SodaBottle

class Menu:
    def __init__(self) -> None:
        self.bottles = []
        self.options = {
            "1": "Add bottle",
            "2": "Show bottles",
            "3": "Save bottle",
            "0": "Exit"
        }

    def display_menu(self) -> None:
        print("Menu:")
        for key, value in self.options.items():
            print(f"{key} - {value}")

    def add_bottle(self) -> None:
        print("Creating soda bottle.")
        brand: str = input("Insert brand: ")
        volume: float = float(input("Insert volume: \n"))
        self.bottles.append(SodaBottle(brand, volume))

    def show_bottles(self) -> None:
        print("#### Soda bottles ####")
        for i, bottle in enumerate(self.bottles, start=1):
            print(f"Bottle {i}:\n  {bottle}")
        print("#### Soda bottles ####\n")

    def select_option(self, choice: str) -> str:
        return self.options.get(choice, "Unknown option, try again.")
