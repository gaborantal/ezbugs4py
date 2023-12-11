## Is it a Triangle?

Create a function named `is_triangle` that takes three integers as parameters. The function should return whether the
three given numbers form a right-angled triangle.

A triangle is right-angled if the Pythagorean theorem holds true. For example, the function should return true for the
following example:
$$
3, 4, 5 => 3^2 + 4^2 = 5^2
$$
But for example, it should return false for 1, 1, 4.

If non-integer numbers are provided as parameters or a number less than or equal to 0 is provided, the function should
return False.
