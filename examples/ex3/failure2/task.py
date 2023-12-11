def coordinate_transform(text, shift):
    transformed = ""
    splitted = text.split(" ")
    i = 0
    while i < len(splitted):
        temp = splitted[i].split(",")
        temp[0] = float(temp[0]) + shift[0]
        temp[1] = float(temp[1]) + shift[1]
        transformed += str(temp[0]) + "," + str(temp[1]) + " "
        i += 1
    return transformed
