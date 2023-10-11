#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0.0

    total_weighted_sum = 0
    total_weight = 0

    for item in my_list:
        score, weight = item
        total_weighted_sum += score * weight
        total_weight += weight

    if total_weight == 0:
        return 0.0
    else:
        return total_weighted_sum / total_weight


# Testing the function with the provided example
my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
result = weight_average(my_list)
print("Average: {:0.2f}".format(result))
