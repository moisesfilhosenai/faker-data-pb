class Position:
    def __init__(self, name, salary_base):
        self.__id = 0
        self.__name = name
        self.__salary_base = salary_base

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def salary_base(self):
        return self.__salary_base
