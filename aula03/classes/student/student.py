from faker_data import fake


class Student:
    def __init__(self):
        self.__id = 0
        self.__name = fake.name()
        self.__email = fake.email()

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email
