def mode(text):
    if not isinstance(text, str) or len(text) == 0:
        return -99
    numbers = text.split(";")
    pairs = dict()
    for number in numbers:
        if number in pairs.keys():
            pairs[number] += 1
        else:
            pairs[number] = 1
    most_num = ""
    for number in pairs:
        if most_num == "":
            most_num = number
        else:
            if pairs[number] >= pairs[most_num]:
                most_num = number
    return int(most_num)
