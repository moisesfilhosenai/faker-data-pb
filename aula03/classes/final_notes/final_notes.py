class FinalNotes:
    def __init__(self, student_id, discipline_id, course_id):
        self.__id = 0
        self.__student_id = student_id
        self.__discipline_id = discipline_id
        self.__course_id = course_id

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
    def course_id(self):
        return self.__course_id
