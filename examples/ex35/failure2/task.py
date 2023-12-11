def proportion(_text, letter):
    piece = 0
    if isinstance(_text, str) or len(_text) > 0 or len(letter) <= 1:
        for fix in _text:
            if letter == fix:
                piece += 1
        return len(_text) / piece
    else:
        return -1
