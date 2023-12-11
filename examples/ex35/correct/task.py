def proportion(text, letter):
    if not isinstance(text, str) or not isinstance(letter, str):
        return -1
    if len(text) == 0:
        return -1
    if len(letter) > 1:
        return -1

    return text.count(letter) / len(text)
