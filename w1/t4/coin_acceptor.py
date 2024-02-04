class CoinAcceptor:
    def __init__(self):
        self.__amount = 0
        self.__value = 0.0
        return None

    def insertCoin(self, value):
        self.__amount += 1
        self.__value += value
        return None

    def getAmount(self):
        return self.__amount

    def returnCoins(self):
        coins_to_return = self.__amount
        self.__amount = 0
        self.__value = 0.0
        return coins_to_return
