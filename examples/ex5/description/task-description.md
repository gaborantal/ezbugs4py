Create a function named `circle` that expects 3 integers as parameters, the three sides of the triangle. The function should return the radius of the circle that can be inscribed around the triangle.

Subtasks:
- Check whether a triangle can be constructed from the three integers (**hint**: each is greater than zero, and the sum of any two sides is greater than the third). If a triangle cannot be constructed from them, return -1.
- The radius of the circumscribed circle can be calculated based on the following formulas:
    * `R = a*b*c/4*T`, where T is the area of the triangle.
    * The area of the triangle can be calculated using Heron's formula: the square root of `(s*(s-a)*(s-b)*(s-c))` (`s = (a+b+c)/2`).
    * (**hint**: in Python, squaring can be done like this: `X**2`. And the square root can be calculated as: `X**0.5`)
