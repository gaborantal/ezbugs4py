## Course

* Write a class named `Course` that represents a university course! The class should have 3 members: `_name`, `_course_code`, and a list called `students`, which will store the Neptun codes of the students enrolled in the course!

* The constructor should take the course name and code as parameters (in that order) and use them to initialize the `_name` and `_course_code` members! The `students` member should be initialized with an empty list!
    * The course code parameter should not be mandatory, with a default value of `UNKNOWN`!

* Create a get and set property for the `_course_code` member, named `course_code`! The getter should return the member’s value **in all uppercase letters**, and the setter should check that the new value is a string type and not an empty string!
    * If the parameter type and value are correct in the setter, set the member to the uppercase version of the value provided in the parameter!
    * If the type or value is incorrect in the setter, set the member’s value to `SOMETHING`!
* Modify the class constructor so that the course code value is set in the same way as in the setter!

* Override the method responsible for converting the object to a string so that it returns text in the following format: `{_name} (code: {_course_code})`! Ensure that the course code is also in all uppercase letters here!

* Create a `list_students` method within the class that takes no parameters and returns a string containing the Neptun codes of the students who have taken the course!
    * If the `students` list is empty, then the method should return the text `No one has taken this course!`
    * Otherwise, join the Neptun codes found in the `students` list with a comma and a space, and return the resulting text! There should be no comma or space after the last Neptun code!

* Override the `+=` operator (`__iadd__` method) in the class, which takes a list of Neptun codes as a parameter!
    * If the list provided in the parameter is empty, throw a `ValueError` exception initialized with the text `Empty list!`
    * If the list provided in the parameter does not exclusively contain string type elements or any string in the list is not exactly 6 characters long, throw a `ValueError` exception initialized with the text `Incorrect Neptun code list!`
    * Otherwise, insert into the end of the `students` list those Neptun codes from the parameter list **that are not already in the list**!

* Override the equality operator! The operator should return true only if all the members of the two courses being compared match exactly!

