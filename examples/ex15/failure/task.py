def length_stat(text):
    res = list()

    if not isinstance(text, str):
        return res

    if text == "":
        return res

    words = text.split(" ")
    length = 0
    for i in range(0, len(words)):
        length += len(words[i])

    average = length / len(words)
    res.append(average)

    count = 0
    for i in range(0, len(words)):
        if len(words[i]) > average:
            count += 1
    res.append(count)

    return res
