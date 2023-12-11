def circle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return -1

    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return -1

    s = (a + b + c) / 2
    t = (s * (s - a) * (s - b) * (s - c)) ** 0.5

    return (a * b * c) / (4 * t)
