from random import randrange
from faker_data import fake


class Seller:
    def __init__(self):
        self.__id = 0
        self.__name = fake.name()
        self.__phone = fake.cellphone_number()
        self.__email = fake.ascii_company_email()
        self.__state = ""
        self.get_estado()

    def get_estado(self):
        estados = [
            "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT",
            "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO",
            "RR", "SC", "SP", "SE", "TO"
        ]
        index = randrange(0, 26)
        self.__state = estados[index]

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def phone(self):
        return self.__phone

    @property
    def email(self):
        return self.__email

    @property
    def state(self):
        return self.__state
