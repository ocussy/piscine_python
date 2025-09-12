class calculator:
    """ Create a calculator class that performs operations on arrays """

    def __init__(self, array):
        """     __init__
        Creates a calculator with an array """
        self.array = array

    def __add__(self, object) -> None:
        """     __add__
        Method that adds a value to all elements of the array """
        tmp = []
        for i in range(len(self.array)):
            tmp.append(self.array[i] + object)
        print(tmp)
        self.array = tmp

    def __mul__(self, object) -> None:
        """     __mul__
        Method that multiplies all elements of the array by a value """
        tmp = []
        for i in range(len(self.array)):
            tmp.append(self.array[i] * object)
        print(tmp)
        self.array = tmp

    def __sub__(self, object) -> None:
        """     __sub__
        Method that subtracts a value from all elements of the array """
        tmp = []
        for i in range(len(self.array)):
            tmp.append(self.array[i] - object)
        print(tmp)
        self.array = tmp

    def __truediv__(self, object) -> None:
        """     __truediv__
        Method that divides all elements of the array by a value """
        tmp = []
        try:
            for i in range(len(self.array)):
                tmp.append(self.array[i] / object)
            print(tmp)
            self.array = tmp
        except ZeroDivisionError as err:
            print("ZeroDivisionbError:", err)
