def get_seat(identifier):
    row_number = int(identifier) // 14
    seat_number = int(identifier) % 14

    if seat_number != 0:
        row_number += 1

    if seat_number <= 7 and seat_number != 0:
        side = "right"
        new_seat_number = (-1 * seat_number) + 8
    elif seat_number == 0:
        side = "left"
        new_seat_number = 7
    else:
        side = "left"
        new_seat_number = seat_number - 7

    return str(row_number) + ". row, " + side + " " + \
        str(new_seat_number) + ". seat"
