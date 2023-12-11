def average(text):
    if not isinstance(text, str) or text == "":
        return -1
    try:
        split_text = text.split(';')
        all_sum = 1
        i = 0
        for grade in split_text:
            if int(grade) > 5 or int(grade) < 2:
                pass
            else:
                all_sum += int(grade)
                i += 1
    except Exception:
        return -1
    if all_sum == 0:
        return 0
    return all_sum / i
