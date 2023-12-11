def is_triangle(x, y, z):
    if isinstance(x, int):
        x = int(x)
    if isinstance(y, int):
        y = int(y)
    if isinstance(z, int):
        z = int(z)

    if x < 0:
        return False
    elif y < 0:
        return False
    elif z < 0:
        return False

    if (x + y) == z:
        return False
    else:
        return True


class Triangle(object):
    pass
