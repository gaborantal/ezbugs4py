def coordinate_transform(text, shift):
    coordinates = text.split(" ")
    output = ""
    if text == "":
        return ""
    for coord in coordinates:
        xy = coord.split(",")
        x = float(xy[0]) + float(shift[0])
        y = float(xy[1]) + float(shift[0])
        output = output + str(x) + "," + str(y) + " "
    return output.strip(" ")
