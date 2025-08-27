def give_bmi(
        height: list[int | float], weight: list[int | float]
        ) -> list[int | float]:

    """
            give_bmi(height, weight)
        Calculate the BMI with a list of height and weight
        (IMC in french) and put it in a tab
    """
    if len(height) != len(weight):
        raise ValueError("Heights and weights needs to have the same lenght.")
    tab = []
    for i in range(len(height)):
        tab.append(weight[i] / (height[i] * height[i]))
    return tab


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:

    """
        apply_limit(bmi, limit)
        Takes the tab with all the BMI and return False
        if the BMI is under the limit and return True otherwise
    """
    tab = []
    for i in range(len(bmi)):
        if bmi[i] > limit:
            tab.append(True)
        else:
            tab.append(False)
    return tab
