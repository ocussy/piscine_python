class calculator:
    """ Create a calculator class with static methods for vector operations """

    @staticmethod
    def dotproduct(a, b) -> None:
        """     dotproduct
        Method that calculates the dot product of two vectors """
        result = sum(float(x) * float(y) for x, y in zip(a, b))
        print("Dot product is:", result)

    @staticmethod
    def add_vec(a, b) -> None:
        """     add_vec
        Method that adds two vectors element by element """
        result = [float(x) + float(y) for x, y in zip(a, b)]
        print("Add Vector is:", result)

    @staticmethod
    def sous_vec(a, b) -> None:
        """     sous_vec
        Method that subtracts two vectors element by element """
        result = [float(x) - float(y) for x, y in zip(a, b)]
        print("Sous Vector is:", result)
