from faker_data import fake


class Employee:
    def __init__(self):
        full_address = f"{fake.street_address()} | {fake.neighborhood()} | {fake.estado_nome()} | {fake.estado_sigla()} | {fake.postcode()}"
        self.__id = 0
        self.__name = fake.name()
        self.__address = full_address

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def address(self):
        return self.__address
