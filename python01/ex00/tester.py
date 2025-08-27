from give_bmi import give_bmi, apply_limit


height = [2.71, 1.15]
weight = [165.3, 38.4]

bmi = give_bmi(height, weight)

print(give_bmi.__doc__)
print(bmi, type(bmi))

print(apply_limit.__doc__)
print(apply_limit(bmi, 26))
