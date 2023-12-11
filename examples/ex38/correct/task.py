from typing import Dict, Tuple, List


def pixel_art(size: int, pixels: Dict[Tuple[int, int], str]):
    board: List[List[str]] = []
    for y in range(size):
        row = []
        for x in range(size):
            row.append(pixels.get((x, y), '.'))
        board.append(row)

    text = ''
    for row in board:
        for pixel in row:
            text += pixel
        text += '\n'
    return text
