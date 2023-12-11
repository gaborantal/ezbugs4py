def circle(a: int, b: int, c: int):
    if (a < 1) or (b < 1) or (c < 1):
        return -1
    elif (a + b <= c) or (a + c <= b) or (b + c <= a):
        return -1
    s = (a + b + c) / 2
    t = (s * (s - a) * (s - b) * (s - c))
    return a * b * c / 4 * t
