def descending_order(num):
    return int("".join(sorted([n for n in str(num)], reverse=True)))
