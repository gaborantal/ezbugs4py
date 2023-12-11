def circle(a, b, c):
    if a > 0 and b > 0 and c > 0 and a + b > c or a + c > b or b + c > a:
        s = (a + b + c) / 2
        T = (s * (s - a) * (s - b) * (s - c))
        R = a * b * c / 4 * T
        return R

    else:
        return -1
