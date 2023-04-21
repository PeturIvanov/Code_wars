import re


def count_smileys(arr):
    pattern = r"(?P<smiling_face>[:|;][-|~]?[\)|D])"
    count = 0
    for emoji in arr:
        match = re.match(pattern, emoji)
        if match:
            count += 1
    return count
