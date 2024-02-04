from menu import Menu

class Main:
    def __init__(self) -> None:
        print("Program starting.")
        self.menu = Menu()
        self.run()
        print("Program ending.")
        return None

    def run(self) -> None:
        while True:
            self.menu.display_menu()
            choice: str = input("Your choice: ")

            if choice == "0":
                print("\nExiting program.")
                break

            action: str = self.menu.select_option(choice)
            if action in self.menu.options.values():
                print(f"'{action}' not implemented yet.\n")
            else:
                print(action)
        return None

if __name__ == "__main__":
    app = Main()
