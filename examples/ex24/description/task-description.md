- Create a class named `Teacher` that has 3 data members: `name` (string), `_retirement_year` (integer), and `teaches` (
  dictionary).

The constructor receives the name and retirement year as parameters, and initializes the `name` and `_retirement_year`
data members with these. The `_retirement_year` data member should not be mandatory to provide, its default value should
be 2062. The `teaches` data member should be initialized with an empty dictionary.

Create a get and set property for the `_retirement_year` data member, named `retirement_year`. The getter should return
the value of the data member, and the setter should set the value of the data member to the value received in the
parameter, provided it is an integer and not less than 1970. In other cases, the setter should do nothing.

Write a `teaches_new_class` method that expects a class name (e.g., `5.a`) and number of students (positive integer) as
parameters. If the types of the parameters are not correct, throw a `ValueError` exception, initialized with the
text `Incorrect parameters!`. If the teacher has not taught this class before, then add it to the `teaches` dictionary (
the key should be the class name, the value the number of students in the class). If he/she has taught it before, then
update the corresponding value (the number of students in the class).

Implement the `>` operator (`__gt__`) in the class, which expects another teacher as a parameter, and returns a logical
value. The operator should return true exactly when the teacher teaches more students than the other teacher received in
the parameter.

Override the function responsible for converting to text so that it returns the teacher's data in the following
format: `The teacher named {name} will retire in {retirement_year}.`.