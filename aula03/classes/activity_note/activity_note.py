from random import randrange


class ActivityNote:
    def __init__(self, student_id, discipline_id):
        self.__id = 0
        self.__student_id = student_id
        self.__discipline_id = discipline_id
        self.__note = randrange(0, 10)
        self.__weight = randrange(1, 5)

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
    def note(self):
        return self.__note

    @property
    def weight(self):
        return self.__weight
