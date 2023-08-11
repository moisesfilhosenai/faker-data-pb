class Course:
    def __init__(self, name, category_course_id):
        self.__id = 0
        self.__name = name
        self.__category_course_id = category_course_id

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def category_course_id(self):
        return self.__category_course_id

    def __str__(self):
        return f"ID: {self.__id}, Name: {self.__name}"
