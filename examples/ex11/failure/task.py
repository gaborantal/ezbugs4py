def is_happy(number: int, checked):
    if checked is None:
        checked = []
    if not isinstance(number, int):
        return None
    if number == 1:
        return True
    elif number is checked:
        return False
    else:
        return is_happy(sum([int(digit) ** 2 for digit in str(number)]),
                        checked + [number])
