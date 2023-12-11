def alliteration(text):
    if not isinstance(text, str):
        return None
    words = text.split(' ')
    if len(words) < 2:
        return None
    prev_letter = ''
    counter = 0
    max_ = 1
    first = True
    for word in words:
        if first:
            prev_letter = word[0].lower()
            first = not first
        current_letter = word[0]
        if prev_letter == current_letter:
            counter += 1
        else:
            if counter > max_:
                max_ = counter
            counter = 1
        prev_letter = current_letter
    if counter > max_:
        max_ = counter
    return max_
