from abc import ABC, abstractmethod


class Weekday(ABC):
    def __init__(self):
        self.index = -1
        self.day_of_the_week = ""
        self.point = 0
        self.is_training_day = False
        self.is_weekend = False
        self.create()

    @abstractmethod
    def create(self):
        pass


class Monday(Weekday):
    def create(self):
        self.index = 0
        self.day_of_the_week = "monday"
        self.point = 1


class Tuesday(Weekday):
    def create(self):
        self.index = 1
        self.day_of_the_week = "tuesday"
        self.point = 1


class Wednesday(Weekday):
    def create(self):
        self.index = 2
        self.day_of_the_week = "wednesday"
        self.point = 3
        self.is_training_day = True


class Thursday(Weekday):
    def create(self):
        self.index = 3
        self.day_of_the_week = "thursday"
        self.point = 1


class Friday(Weekday):
    def create(self):
        self.index = 4
        self.day_of_the_week = "friday"
        self.point = 1


class Saturday(Weekday):
    def create(self):
        self.index = 5
        self.day_of_the_week = "saturday"
        self.point = 2
        self.is_weekend = True


class Sunday(Weekday):
    def create(self):
        self.index = 6
        self.day_of_the_week = "sunday"
        self.point = 2
        self.is_weekend = True


class WeekdayFactory:
    @staticmethod
    def create_weekday(day_of_the_week):
        if day_of_the_week == "monday":
            return Monday()
        elif day_of_the_week == "tuesday":
            return Tuesday()
        elif day_of_the_week == "wednesday":
            return Wednesday()
        elif day_of_the_week == "thursday":
            return Thursday()
        elif day_of_the_week == "friday":
            return Friday()
        elif day_of_the_week == "saturday":
            return Saturday()
        elif day_of_the_week == "sunday":
            return Sunday()
        else:
            return None
