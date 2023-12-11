def mode(text):
    if not isinstance(text, str):
        return -99
    numbers = text.split(",")
    result = 0
    for number in numbers:
        result += number

    result = result / len(numbers)

    return result
