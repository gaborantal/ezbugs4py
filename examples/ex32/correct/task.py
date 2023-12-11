def palindrome_words(param):
    number = 0
    if not isinstance(param, str) or len(param) == 0:
        return -1
    words = param.split(",")
    for word in words:
        if word == word[::-1] and len(word) >= 4 and word.isupper():
            number += 1
    return number
