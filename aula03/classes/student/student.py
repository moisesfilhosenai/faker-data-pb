class Student:
    def __init__(self, name, email):
        self.__id = 0
        self.__name = name
        self.__email = email

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email
