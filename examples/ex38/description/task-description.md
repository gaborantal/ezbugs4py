## Pixel Art

Create a function named `pixel_art` that expects 2 parameters. Both are mandatory. The first one (`size`) is a number,
and the second one is a dictionary of string values indexed with a tuple of two
numbers (`pixels: Dict[Tuple[int, int], str]`). The function transforms the dictionary of pixels into a table-like text.
Each character in every row should be a `'.'` (dot) if the given coordinate is not present in the dictionary. If it is
present, the character should be the pixel itself. The keys of the dictionary are stored in the form of x, y, or column,
row. The origin of the received table is at (0,0), the top-left corner. The `size` also indicates the number of rows and
columns in the square table. If it is 0, the return value should be an empty string (`""`).


