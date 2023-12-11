def dict_complete(test_input):
    result = {}
    if len(test_input) == 0:
        return result
    current = 1
    for key, value in test_input.items():
        if key == current:
            result[key] = value
        else:
            result[current] = 0
        current += 1
    return result
