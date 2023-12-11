def swap(what, onto_what):
    what = what.lower()
    d = {
        "ç": "c",
        "é": "e",
        "ï": "i",
        "à": "a",
        "ô": "o",
        "ñ": "n",
        "ā": "a",
    }
    for punc_mark in d.keys():
        what = what.replace(punc_mark, d[punc_mark])
    list_res = what.split(" ")
    delete = []

    for i, element in enumerate(list_res):
        if len(element) <= 3:
            delete.append(i)
        if element in onto_what:
            list_res[i] = onto_what[element]

    for i in range(len(delete))[::-1]:
        del list_res[delete[i]]

    return "-".join(list_res)
