class Discipline:
    def __init__(self, name, course_id):
        self.__id = 0
        self.__name = name
        self.__course_id = course_id

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def course_id(self):
        return self.__course_id
