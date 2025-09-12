def square(x: int | float) -> int | float:
    """     square(x):
    returns the square of a number"""
    return x ** 2


def pow(x: int | float) -> int | float:
    """     pow(x):
    returns x raised to the power of x"""
    return x ** x


def outer(x: int | float, function) -> object:
    """     outer(x, function):
    returns a closure that applies the function repeatedly to x"""
    count = 0

    def inner() -> float:
        """     inner():
        applies the function count times to the initial value"""
        nonlocal count
        count += 1
        result = x
        for _ in range(count):
            result = function(result)
        return result
    return inner
