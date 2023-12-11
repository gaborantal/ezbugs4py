def average(data):
    if data == "":
        empty = {}
        return empty
    my_list = data.split(";")
    averages = {}
    for student in my_list:
        sum = 0
        count = 0
        name = ""
        first = 0
        elements = student.split(",")
        for element in elements:
            if first == 0:
                name = element
                first = 1
            else:
                sum = sum + element
                count = count + 1
        at = sum / count
        averages[name] = at
    return averages
