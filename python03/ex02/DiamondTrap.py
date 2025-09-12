from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """ Create a class King which inherits
        from both Baratheon and Lannister classes"""

    def __init__(self, first_name, is_alive=True):
        """     __init__
        Creates a King with a name and a status of health state """
        super().__init__(first_name, is_alive)

    def get_eyes(self):
        """     get_eyes
        Method that returns the eye color of the king """
        return self.eyes

    def get_hairs(self):
        """     get_hairs
        Method that returns the hair color of the king """
        return self.hair

    def set_eyes(self, eyes):
        """     set_eyes
        Method that sets the eye color of the king """
        self.eyes = eyes

    def set_hairs(self, hair):
        """     set_hairs
        Method that sets the hair color of the king """
        self.hair = hair
