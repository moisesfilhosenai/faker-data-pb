from faker_data import fake


class Customer:
    def __init__(self):
        self.__id = 0
        self.__name = fake.name()
        self.__zipcode = fake.postcode()
        self.__country = fake.city()
        self.__state = fake.state()

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def zipcode(self):
        return self.__zipcode

    @property
    def country(self):
        return self.__country

    @property
    def state(self):
        return self.__state
