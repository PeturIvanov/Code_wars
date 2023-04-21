def valid_ISBN10(isbn):
    if len(isbn) == 10 and isbn[:-1].isdigit():
        total_sum = sum([int(n) * (i + 1) for i, n in enumerate(isbn[:-1])])
        if isbn[-1].isdigit():
            total_sum += int(isbn[-1]) * 10
        elif isbn[-1] == "X":
            total_sum += 10 * 10
        else:
            return False
        if total_sum % 11 == 0:
            return True
        else:
            return False
    else:
        return False

