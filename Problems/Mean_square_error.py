def solution(array_a, array_b):
    differences = []
    for i in range(len(array_a)):
        diff = (abs(array_a[i] - array_b[i])) ** 2
        differences.append(diff)
    return sum(differences) / len(array_a)
