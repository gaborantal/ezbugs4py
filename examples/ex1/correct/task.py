def dict_complete(test_input: dict):
    value = dict()
    if len(test_input) == 0:
        return value
    else:
        length = 0
        for dict_key, dict_value in test_input.items():
            if length < dict_key:
                length = dict_key
        for dict_key in range(0, length):
            dict_key += 1
            value[dict_key] = 0
        for dict_key, dict_value in test_input.items():
            value[dict_key] = dict_value
        return value
