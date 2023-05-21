# Zebra emulation program
# Page footplayer
# Stage 22 (Basic task)
# Subject theme: Python Object-Oriented Programming. Send Messages and Code Reuse
# Version: 1.0
# Autor: Ilja
# Date: 10.05.2023


class FootballPlayer:
    def __init__(self, name='no name', surname='', goal='1', assist='1'):
        self.__name = name
        self.__surname = surname
        self.__goal = goal
        self.__assist = assist

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self.__name = name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if isinstance(surname, str):
            self.__surname = surname

    @property
    def goal(self):
        return self.__goal

    @goal.setter
    def goal(self, goal):
        if isinstance(goal, int) and goal > 0:
            self.__goal = goal

    @property
    def assist(self):
        return self.__assist

    @assist.setter
    def assist(self, assist):
        if isinstance(assist, int) and assist > 0:
            self.__assist = assist

    def __str__(self):
        return (f"{self.surname} {self.name}: "
                f"goals = {self.goal}, assists = {self.assist}")
