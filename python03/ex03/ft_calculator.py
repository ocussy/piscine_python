class calculator:
    def __init__(self, array):
        self.array = array

    def __add__(self, object) -> None:
        x2 = []
        for i in range(len(self.array)):
            x2.append(self.array[i] + object)
        print(x2)
        self.array = x2

    def __mul__(self, object) -> None:
        x2 = []
        for i in range(len(self.array)):
            x2.append(self.array[i] * object)
        print(x2)
        self.array = x2

    def __sub__(self, object) -> None:
        x2 = []
        for i in range(len(self.array)):
            x2.append(self.array[i] - object)
        print(x2)
        self.array = x2

    def __truediv__(self, object) -> None:
        x2 = []
        try:
            for i in range(len(self.array)):
                x2.append(self.array[i] / object)
            print(x2)
            self.array = x2
        except ZeroDivisionError as err:
            print("ZeroDivisionbError:", err)
