# Imports
from counter import Counter

# Main program structure
class Main:
    def __init__(self) -> None:
        print("Program starting.\nInitializing counter...")
        
        print("Counter initialized.")
        self.counter = Counter()
        self.run()
        print("\nProgram ending.")
        return None

    def run(self):
        while True:
            print("\nOptions:")
            print("1) Add count")
            print("2) Get count")
            print("3) Zero count")
            print("0) Exit program")

            choice = input("Choice: ")
            if choice == "1":
                self.counter.addCount()
                print("Count increased")
            elif choice == "2":
                print(f"Current count '{self.counter.getCount()}'")
            elif choice == "3":
                self.counter.zeroCount()
                print("Count zeroed")
            elif choice == "0":
                break
            else:
                print("Invalid option. Please try again.")
        return None
    

if __name__ == "__main__":
    app = Main()
    
    