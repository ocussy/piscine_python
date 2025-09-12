def mean(data: list[float]) -> float:
    """     mean(list):
    returns the mean between a list of numbers"""
    return sum(data) / len(data)


def median(data: list[float]) -> float:
    """     median(list):
    returns the median of a list of numbers"""
    n = len(data)
    mid = n // 2
    if n % 2 == 0:
        return (data[mid - 1] + data[mid]) / 2
    return data[mid]


def quartiles(data: list[float]) -> list[float]:
    """     quartiles(list):
    returns the first and third quartiles of a list of numbers"""
    n = len(data)
    q1 = float(data[int((n + 3) / 4) - 1])
    q3 = float(data[int((3 * n + 1) / 4) - 1])
    return [q1, q3]


def variance(data: list[float]) -> float:
    """     variance(list):
    returns the variance of a list of numbers"""
    m = mean(data)
    return sum((x - m) ** 2 for x in data) / len(data)


def std_dev(data: list[float]) -> float:
    """     std_dev(list):
    returns the standard deviation of a list of numbers"""
    return variance(data) ** 0.5


def ft_statistics(*args, **kwargs) -> None:
    """     ft_statistics(*args, **kwargs):
    performs statistical operations on a list
    of numbers based on keyword arguments"""
    data = sorted(args)

    operations = {
        "mean": lambda d: f"mean: {mean(d)}",
        "median": lambda d: f"median: {median(d)}",
        "quartile": lambda d: f"quartile: {quartiles(d)}",
        "var": lambda d: f"var: {variance(d)}",
        "std": lambda d: f"std: {std_dev(d)}"
    }

    for op in kwargs.values():
        if not args:
            print("ERROR")
        elif op in operations:
            print(operations[op](data))
