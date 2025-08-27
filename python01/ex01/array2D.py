import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
            slice_me(family, start, end)
        Takes a list of lists and give the shape of it
        Then slice the tab with the start and end values
        Return the new tab of it
    """
    for i in family:
        if not isinstance(i, list):
            raise TypeError("Type error in the array")
    if len(set(len(row) for row in family)) != 1:
        raise ValueError("All rows must have the same size")
    print("My shape is :", np.shape(family))
    newFamily = family[start:end]
    print("My new shape is : ", np.shape(newFamily))
    return newFamily
