def twice(a):
    my_list = a.strip().split(",")
    name = dict
    for element in my_list:
        if element not in name:
            name[element] = 0
        name[element] += 1
    output = []
    for key, value in name.items():
        if value == 2:
            output.append(key)
    return output
