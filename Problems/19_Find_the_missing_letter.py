from string import ascii_letters


# This function accepts  consecutive (increasing) letters.
def find_missing_letter(chars):
    start_index = ascii_letters.index(chars[0])
    end_index = ascii_letters.index(chars[-1])
    substring = ascii_letters[start_index:end_index + 1]
    for el in substring:
        if el not in chars:
            return el
