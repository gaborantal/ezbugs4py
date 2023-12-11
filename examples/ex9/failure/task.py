def word_count(text):
    if not isinstance(text, str):
        return {}
    result = {}
    for token in text.split():
        count = result[token] if token in result else 0
        result[token] = count
    return result
