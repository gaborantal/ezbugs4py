def is_triangle(a, b, c):
    if isinstance(a, int) and isinstance(b, int) and isinstance(c, int):
        if a > 0 and b > 0 and c > 0:
            if (a * a) + (b * b) == c * c:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
