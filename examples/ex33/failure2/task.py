def swap(text, dict):
    list = text.split(' ')
    retStr = ""

    for item in list:
        item.lower()

        item = item.replace('ç', 'c'). \
            replace('é', 'e'). \
            replace('ï', 'i'). \
            replace('à', 'a'). \
            replace('ô', 'o'). \
            replace('ñ', 'n'). \
            replace('ā', 'a')

        if item in dict.keys():
            item = dict.get(item)

        if len(item) < 4:
            item = ''

    for item in list:
        if item != '':
            retStr += item

        if list[len(list) - 1] != item:
            retStr += '-'

    return retStr
