def length_stat(text):
    if(text == "" or text == " " or not isinstance(text, str)):
        return []

    print(text)
    list_ = text.split(" ")
    i = 0
    j = 0
    for elem in list_:
        for elem2 in elem:
            i = i + 1

    number = int (i / len(list_))

    for elem in list_:
        if(len(elem) > number):
            j = j + 1

    lis = (number, j)
    print(lis)
    return lis

