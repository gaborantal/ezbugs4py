## Where is my seat?

Our favorite Winnie the Pooh movie is playing in the giant hall of the city's *Retro Fox cinema*, which promises to be
unmissable.

The cashier gladly explained that their system still follows the traditional method, meaning the numbering starts from
the center aisle on both sides. So, on the left and right, you can find the 1st seat, and then the seat number increases
continuously inward. Along the wall, you can always find the 7th seat.

The ticket system is not the most modern; it can't even print on the ticket, saying "Row 5, Seat 3." Instead, we get the
continuous identification of seats, such as 59. There are 14 seats in each row in the hall, and **we don't know how many
rows there are in total** (the hall is so big that you can't see [it's not for nothing it's a giant hall]).

Our forgetful friend unfortunately forgot where he asked for the tickets. Let's help him! Let's create the function
called `get_seat` that takes the continuous seat ID of the ticket and returns where the seat is located.

The function should return where the given seat is, in the following format: `{row}. row, {side} {number}. seat.` We
don't
need to worry about checking the parameter; we will definitely get the correct one.

So, for example, if the function receives the parameter `21`, it `should return 2nd row, right 1st seat`.
