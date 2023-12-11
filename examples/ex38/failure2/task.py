def pixel_art(size, pixels):
    for i in range(size):
        output = ""
        for j in range(size):
            if pixels.get((i, j)) is not None:
                output += (str(pixels.get((i, j))))
            else:
                output += "."
        return output
