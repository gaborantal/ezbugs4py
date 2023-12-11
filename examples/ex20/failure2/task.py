def word_statistics(text):
    dictionary = dict()
    if not isinstance(text, str):
        return dictionary
    new_text = text.split(' ')
    if len(new_text) < 2:
        return dictionary
    number_of_words = len(new_text)
    sum = 0
    count = 0
    for x in new_text:
        print(len(x))
        sum += len(x)
    average_length = int(sum / number_of_words)

    for x in new_text:
        if len(x) > average_length:
            count += 1

    dictionary['number_of_words'] = number_of_words
    dictionary['average_length'] = average_length
    dictionary['long_words'] = count
