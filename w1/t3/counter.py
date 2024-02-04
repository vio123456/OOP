class Counter:
    def __init__(self):
        self.__count = 0

    def addCount(self):
        self.__count += 1
        
        return None

    def getCount(self):
        return self.__count

    def zeroCount(self):
        self.__count = 0
        
        return None

