class calculator:

    @staticmethod
    def dotproduct(a, b) -> None:
        result = sum(float(x) * float(y) for x, y in zip(a, b))
        print("Dot product is:", result)

    @staticmethod
    def add_vec(a, b) -> None:
        result = [float(x) + float(y) for x, y in zip(a, b)]
        print("Add Vector is:", result)

    @staticmethod
    def sous_vec(a, b) -> None:
        result = [float(x) - float(y) for x, y in zip(a, b)]
        print("Sous Vector is:", result)
