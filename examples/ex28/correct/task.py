def threetimes(names):
    names_list = names.split(",")

    for i in range(len(names_list)):
        names_list[i] = names_list[i].lstrip()

    names_count = dict()

    for i in range(len(names_list)):
        names_count[names_list[i]] = names_count.get(names_list[i], 0) + 1

    result = []

    for key, value in names_count.items():
        if value == 3:
            result.append(key)

    return result
