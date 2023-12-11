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
            i += 1
        res.append(" ".join(str))
    if i < len(sliced):
        str = []
        ii = i
        for j in range(ii, len(sliced)):
            str.append(sliced[i])
            i += 1
        res.append(" ".join(str))
    return res
