class Discipline:
    def __init__(self, name):
        self.__id = 0
        self.__name = name

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def course_id(self):
        return self.__course_id
