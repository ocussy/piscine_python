class calculator:
    def __init__(self, array):
        self.array = array

    def __add__(self, object) -> None:
        tmp = []
        for i in range(len(self.array)):
            tmp.append(self.array[i] + object)
        print(tmp)
        self.array = tmp

    def __mul__(self, object) -> None:
        tmp = []
        for i in range(len(self.array)):
            tmp.append(self.array[i] * object)
        print(tmp)
        self.array = tmp

    def __sub__(self, object) -> None:
        tmp = []
        for i in range(len(self.array)):
            tmp.append(self.array[i] - object)
        print(tmp)
        self.array = tmp

    def __truediv__(self, object) -> None:
        tmp = []
        try:
            for i in range(len(self.array)):
                tmp.append(self.array[i] / object)
            print(tmp)
            self.array = tmp
        except ZeroDivisionError as err:
            print("ZeroDivisionbError:", err)
