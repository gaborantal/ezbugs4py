## Happy numbers

A happy number is a positive integer for which it is true that if we calculate the sum of the squares of its digits and
repeat this process as needed until we get a single-digit number, the result will be 1. In the case of an infinite loop,
the number is not happy. For example, 23 is a happy number because `2^2 + 3^2 = 4+9 = 13, 1^2 + 3^2 = 1 + 9 = 10, 1^2 +
0^2 = 1 + 0 = 1.`

Create a function named `is_happy` that takes an integer and a list of previously tested values as parameters. The
function should return whether the given number is a happy number. If the parameter is not an integer, the function
should return `None`.
### Hint

The sum of the squares of the digits can lead to an infinite loop. It is advisable to store the previously checked
numbers:  `is_happy(number: int, checked: typing.List[int] = [])`.
