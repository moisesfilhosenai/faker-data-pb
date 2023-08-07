class Benefit:
    def __init__(self, name, price):
        self.__id = 0
        self.__name = name
        self.__price = price

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price
