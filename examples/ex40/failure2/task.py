def get_seat(total_seats):
    seats_per_row = 14

    if total_seats > seats_per_row:
        row = int(total_seats / seats_per_row)
        seat = total_seats - (row * seats_per_row)
        if seat > 7:
            side = 'right'
        else:
            side = 'left'

        if side != 'left':
            seat = seat - 7
        else:
            seat = 7 - seat + 1
    else:
        row = 1
        if total_seats > 7:
            side = 'right'
            seat = total_seats - 7
        else:
            side = 'left'
            seat = 7 - (7 - total_seats)
    row = str(row)
    seat = str(seat)
    result = "{row}. row, {side} side, {seat}. seat."
    return result
