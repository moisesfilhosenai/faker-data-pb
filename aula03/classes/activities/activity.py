from random import randint


class Activity:
    def __init__(self, description, discipline_id):
        self.__id = 0
        self.__description = description
        self.__discipline_id = discipline_id
        self.__available = randint(3, 10)

    @property
    def id(self):
        return self.__id

    @property
    def description(self):
        return self.__description

    @property
    def discipline_id(self):
        return self.__discipline_id

    @property
    def available(self):
        return self.__available

