from random import randrange


class HumnanResource:
    def __init__(self, employee_id, benefit_id, position_id, month, year):
        self.__id = 0
        self.__employee_id = employee_id
        self.__benefit_id = benefit_id
        self.__position_id = position_id
        self.__tax = randrange(3, 11)
        self.__total_hours_late = randrange(2, 32)
        self.__month = month
        self.__year = year

    @property
    def id(self):
        return self.__id

    @property
    def employee_id(self):
        return self.__employee_id

    @property
    def benefit_id(self):
        return self.__benefit_id

    @property
    def position_id(self):
        return self.__position_id

    @property
    def tax(self):
        return self.__tax

    @property
    def total_hours_late(self):
        return self.__total_hours_late

    @property
    def month(self):
        return self.__month

    @property
    def year(self):
        return self.__year

