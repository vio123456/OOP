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
            elif choice == "1":
                self.menu.add_bottle()
            elif choice == "2":
                self.menu.show_bottles()
            elif choice == "3":
                print("'Save bottle' not implemented yet.")
            else:
                print("Unknown option, try again.")
        return None

if __name__ == "__main__":
    app = Main()