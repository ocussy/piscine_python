from abc import ABC, abstractmethod


class Character(ABC):
    def __init__(self, first_name, is_alive=True):
        """ Creates a character with a name
        and a status of health state (True/False) """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        pass


class Stark(Character):
    """ Creates a Stark which inherits of Character class """

    def die(self):
        """ Method that passes is_alive from True to False"""
        self.is_alive = False
