from coin_acceptor import CoinAcceptor

class Main:
    def __init__(self)-> None:
        print("Program starting.")
        self.coin_acceptor = CoinAcceptor()
        self.run()
        print("Program ending.")
        return None

    def run(self):
        while True:
            print("1 - Insert coin")
            print("2 - Show coins")
            print("3 - Return coins")
            print("0 - Exit program")
            
            choice = input("Your choice: ")

            if choice == "1":
                # Assuming each inserted coin has a predefined value, e.g., 1.0
                self.coin_acceptor.insertCoin(1.0)
                print("")
            elif choice == "2":
                print(f"Currently '{self.coin_acceptor.getAmount()}' coins in coin acceptor\n")
            elif choice == "3":
                returned_coins = self.coin_acceptor.returnCoins()
                print(f"Coin acceptor returned '{returned_coins}' coins.\n")
            elif choice == "0":
                break
            else:
                print("Invalid choice. Please try again.\n")
        return None

if __name__ == "__main__":
    app = Main()
