def method_decorator(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return wrapper


class calculator:

    @method_decorator
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        result = 0
        for x, y in zip(V1, V2):
            result += x * y
        print("Dot product is:", result)

    @method_decorator
    def add_vec(V1: list[float], V2: list[float]) -> None:
        result = []
        for x, y in zip(V1, V2):
            result.append(x + y)
        print("Add Vector is:", result)

    @method_decorator
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        result = []
        for x, y in zip(V1, V2):
            result.append(x - y)
        print("Sous Vector is:", result)
