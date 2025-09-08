from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """ Create a class King which inherits
        from both Baratheon and Lannister classes"""

    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)

    def get_eyes(self):
        return self.eyes

    def get_hairs(self):
        return self.hair

    def set_eyes(self, eyes):
        self.eyes = eyes

    def set_hairs(self, hair):
        self.hair = hair
