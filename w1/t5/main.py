from coin_acceptor import CoinAcceptor

class Main:
    def __init__(self)-> None:
        print("Program starting.")
        print("Welcome to coin acceptor program.")
        print("Insert new coin by typing it's value (0 returns the money, -1 exits the program)\n")
        self.coin_acceptor = CoinAcceptor()
        self.run()

        print("\nProgram ending.")
        return None

    def run(self):
        while True:
            user_input = input("Insert coin(0 return, -1 exit): ")
            try:
                coin_value = float(user_input)
                if coin_value == -1:
                    print("Exiting program.")
                    break
                elif coin_value == 0:
                    coins, value = self.coin_acceptor.returnCoins()
                    print("Returning coins...\n{} coins with {}€ value returned.".format(coins, self.format_value(value)))
                    print("Inserted coins - {}, value - {}€\n".format(self.coin_acceptor.getAmount(), self.format_value(self.coin_acceptor.getValue())))
                else:
                    self.coin_acceptor.insertCoin(coin_value)
                    print("Inserting...\nInserted coins - {}, value - {}€\n".format(self.coin_acceptor.getAmount(), self.format_value(self.coin_acceptor.getValue())))
            except ValueError:
                print("Invalid input. Please enter a valid number.\n")
        return None
    
    def format_value(self, value):
         return "0" if value == 0 else "{:.1f}".format(value)
if __name__ == "__main__":
    app = Main()
