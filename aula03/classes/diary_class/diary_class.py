from random import randrange
from datetime import datetime
from faker_data import fake


class DiaryClass:
    def __init__(self, student_id, discipline_id):
        self.__id = 0
        self.__student_id = student_id
        self.__discipline_id = discipline_id
        self.__data = fake.date_between_dates(datetime(2015, 1, 1), datetime(2020, 12, 31)).strftime("%d/%m/%Y")
        self.__number_absences = randrange(0, 10)

    @property
    def id(self):
        return self.__id

    @property
    def student_id(self):
        return self.__student_id

    @property
    def discipline_id(self):
        return self.__discipline_id

    @property
    def data(self):
        return self.__data

    @property
    def number_absences(self):
        return self.__number_absences
