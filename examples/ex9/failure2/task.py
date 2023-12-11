def word_count(text):
    dict = {}
    if isinstance(text, str):
        for words in text:
            word = words.strip(".,_ ")
            if word not in dict:
                dict[word] = 0
            dict[word] += 1
            return dict
    else:
        return {}
