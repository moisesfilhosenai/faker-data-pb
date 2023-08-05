class Product:
    def __init__(self, name, category, price):
        self.__id = 0
        self.__name = name
        self.__category = category
        self.__price = float(price)

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def category(self):
        return self.__category

    @property
    def price(self):
        return self.__price

