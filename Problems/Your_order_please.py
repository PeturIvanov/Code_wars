def order(sentence):
    words = sentence.split()
    number = 1
    result = []
    while len(result) < len(words):
        for word in words:
            if str(number) in word:
                result.append(word)
                number += 1
    return " ".join(result)
