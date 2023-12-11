def filter(_text: str) -> list:
    if not isinstance(_text, str) or len(_text) == 0:
        return list()

    words = _text.split(',')
    average = sum(len(word) for word in words) / len(words)
    return [word.upper()[::-1] for word in words if len(word) > average]
