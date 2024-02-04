
class Menu:
    def __init__(self) -> None:
        self.options = {
            "1": "Add bottle",
            "2": "Show bottle",
            "3": "Save bottle",
            "0": "Exit"
        }

    def display_menu(self) -> None:
        print("Menu:")
        for key, value in self.options.items():
            print(f"{key} - {value}")

    def select_option(self, choice: str) -> str:
        return self.options.get(choice, "Unknown option, try again.\n")