def word_statistics(text: str) -> dict:
    if not isinstance(text, str) or len(text.split()) < 2:
        return {}

    words = text.split()
    
    number_of_words = len(words)
    average_length = int(sum([len(word) for word in words]) / number_of_words)
    long_words = len([word for word in words if len(word) > average_length])

    return {'number_of_words': number_of_words, 'average_length': average_length, 'long_words': long_words}