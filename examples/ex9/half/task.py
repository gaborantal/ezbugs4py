def word_count(text):
    if isinstance(text, str):
        counts = dict()
        words = text.split(" ")
        unique_words = {}
        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
        return counts
