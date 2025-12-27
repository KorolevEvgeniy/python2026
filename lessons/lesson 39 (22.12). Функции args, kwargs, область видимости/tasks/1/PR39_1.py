def mean_abs_deviation(*scores):
    if len(scores) == 0:
        raise ValueError("Нужно ввести хотя бы один балл")
    
    average = sum(scores) / len(scores)
    
    deviations = []
    for score in scores:
        deviation = abs(score - average)
        deviations.append(round(deviation, 1))
    return tuple(deviations)

print(mean_abs_deviation(3, 5, 7, 9))
# input: 3, 5, 7, 9
# steps: avg = 6.0, deviations = (3.0, 1.0, 1.0, 3.0)
# output: (3.0, 1.0, 1.0, 3.0)

