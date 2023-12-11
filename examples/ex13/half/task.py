def groupby(input: dict):
    output = {}
    for key, value in input.items():
        output[value] = output.get(value, []) + [key]
    return output
