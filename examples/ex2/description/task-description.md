Create a class named `Triangle` that represents a triangle. The class should have three data members: `_a`, `b`, and `c`. The initializer function should expect three parameters, the second and third of which should be optional. The first parameter is the a side, the second is `b`, and the third is `c`. If the `b` or `c` side is not specified, then its value should also be the value of `a`. **Store the changes in the `a_values` array**, i.e., when the value changes, put the new value in the array. Pay attention to also include the value specified first when creating the object.

- Create a property for the `a` value. The name of the property should be `a`. If we do not pass an integer, it should throw an error, which is an `Exception` type exception, initialized with the text `Invalid value`. Don’t forget to track the changes of the `a` values in an array.

- Create a function named `area` that returns the area of the triangle. (`s = (a+b+c) / 2`; `T = sqrt(s*(s-a)*(s-b)*(s-c))`).

- Create a function named `perimeter` that returns the perimeter of the triangle. (`k = (a + b + c)`).

- Override the equality operator (`==`). Two triangles are equal if both their perimeter and area are the same.

- Override the function that implements the conversion to text so that the triangle returns the number of changes in the a value in the following form: `The changes in the a values, {number of changes in the a values}`, where `{number of changes in the a values}` is the length of the list used to denote the change in the `a` value.
