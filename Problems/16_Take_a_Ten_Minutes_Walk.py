# This function accepts directions ("w", "e", "s", "n")
def is_valid_walk(walk):
    flag = True
    if len(walk) != 10:
        flag = False
    else:
        if walk.count("e") != walk.count("w") or walk.count("n") != walk.count("s"):
            flag = False
    return flag
