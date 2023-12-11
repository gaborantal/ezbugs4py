def filter(text):
    add = 0
    counter = 0

    filter_list = text.split(',')
    for i in filter_list:
        add += len(i.toUpper)
        counter = len(filter_list)

    average = add / (counter - 1)
    for i in filter_list:
        if len(i) > average:
            reversed(i)
