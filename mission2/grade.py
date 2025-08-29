from abc import ABC, abstractmethod


class Grade(ABC):
    def __init__(self):
        self.key = -1
        self.name = ""
        self.cut_line = -1
        self.create()

    @abstractmethod
    def create(self):
        pass


class GoldGrade(Grade):
    def create(self):
        self.key = 1
        self.name = "GOLD"
        self.cut_line = 50


class SilverGrade(Grade):
    def create(self):
        self.key = 2
        self.name = "SILVER"
        self.cut_line = 30


class NormalGrade(Grade):
    def create(self):
        self.key = 0
        self.name = "NORMAL"
        self.cut_line = 0


class GradeFactory:
    @staticmethod
    def create_grade(name):
        if name == "GOLD":
            return GoldGrade()
        elif name == "SILVER":
            return SilverGrade()
        else:
            return NormalGrade()
