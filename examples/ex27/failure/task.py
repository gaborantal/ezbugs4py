def split(text, my_list=-1):
    if my_list == -1:
        return [text]
    res = []
    sliced = text.split(" ")
    i = 0
    for textLength in my_list:
        str = []
        for j in range(textLength):
            if i == len(sliced):
                return []
            str.append(sliced[i])
        res.append(" ".join(str))
    if i < len(sliced):
        str = []
        for j in range(i, len(sliced)):
            str.append(sliced[i])
        res.append(" ".join(str))
    i += 1
    return res
