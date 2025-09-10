from S1E9 import Character


class Baratheon(Character):
    """ Creates a Baratheon class which inherits
        of the Character class"""
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hair = "dark"

    def __str__(self):
        return (
            f"{self.first_name} {self.family_name} has "
            f"{self.hair} hair and {self.eyes} eyes"
        )

    def __repr__(self):
        return (f"Baratheon(family_name={self.family_name},"
                f"hair={self.hair}, eyes={self.eyes})")

    def die(self):
        """ Method that passes is_alive from True to False"""
        self.is_alive = False


class Lannister(Character):
    """ Creates a Lannistern class which inherits
        of the Character class"""
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hair = "light"

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        return cls(first_name, is_alive)

    def __str__(self):
        return (
            f"{self.first_name} {self.family_name} has "
            f"{self.hair} hair and {self.eyes} eyes"
        )

    def __repr__(self):
        return (f"Lannister(family_name={self.family_name},"
                f"hair={self.hair}, eyes={self.eyes})")

    def die(self):
        """ Method that passes is_alive from True to False"""
        self.is_alive = False
