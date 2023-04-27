from itertools import combinations


# This function accepts list of integers.
def powerset(nums):
    result = []
    for n in range(len(nums) + 1):
        all_combinations = combinations(nums, n)
        for x in all_combinations:
            result.append(list(x))
    return result
