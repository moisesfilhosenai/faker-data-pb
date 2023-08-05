from random import randrange
from datetime import datetime
from faker_data import Faker

fake = Faker("pt_BR")


class Order:
    def __init__(self, customer_id, seller_id, product_id, product_price, quantity):
        self.__id = randrange(35, 29667430)
        self.__data = fake.date_between_dates(datetime(2015, 1, 1), datetime(2020, 12, 31)).strftime("%d/%m/%Y")
        self.__customer_id = customer_id
        self.__seller_id = seller_id
        self.__product_id = product_id
        self.__quantity = quantity
        self.__price = product_price

    @property
    def id(self):
        return self.__id

    @property
    def data(self):
        return self.__data

    @property
    def customer_id(self):
        return self.__customer_id

    @property
    def seller_id(self):
        return self.__seller_id

    @property
    def produt_id(self):
        return self.__product_id

    @property
    def quantity(self):
        return self.__quantity

    @property
    def price(self):
        return self.__price
