from random import randint


class Note:
    def __init__(self, student_id, activity):
        self.__id = 0
        self.__student_id = student_id
        self.__activity_id = activity["id"]
        self.__available = randint(0, activity["available"])

    @property
    def id(self):
        return self.__id

    @property
    def student_id(self):
        return self.__student_id

    @property
    def activity_id(self):
        return self.__activity_id

    @property
    def available(self):
        return self.__available
