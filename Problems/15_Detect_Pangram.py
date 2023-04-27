from string import ascii_lowercase


# This function accepts text.
def is_pangram(s):
    for char in ascii_lowercase:
        if char not in s.lower():
            return False
        else:
            continue
    return True
