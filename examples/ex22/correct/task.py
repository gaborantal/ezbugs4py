def twice(inp):
    inp = inp.replace(" ", "")
    my_list = inp.split(",")
    result = []
    for item in my_list:
        counter = 0
        for i in my_list:
            if i == item:
                counter += 1
        if counter == 2:
            result.append(item)
            my_list.remove(item)
    return result
