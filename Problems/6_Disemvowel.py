def disemvowel(string):
    result = ""
    for char in string:
        if char.lower() not in ["a", "e", "i", "o", "u"]:
            result += char
    return result

