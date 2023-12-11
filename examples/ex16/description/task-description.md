## Film

* Create a class named `Film` with 3 attributes: `_title`, `length`, and a list named `ratings`.

* The constructor should receive the title and length as parameters (in that order) and use them to initialize the `_title` and `length` attributes. The `length` should not be mandatory to provide, with a default value of 60. The `ratings` attribute should be initialized with an empty list.

* Create get and set properties for the `_title` attribute, named `title`. The getter should return the attribute’s value, and the setter should set the attribute’s value to the provided parameter if it is of string type. If the type is different, the setter should do nothing.

* Write a method named `add_rating` that expects a rating as a parameter. If the rating is a floating-point number between 1.0 and 10.0, then insert it at the end of the `ratings` list. If the parameter is inappropriate, throw an Exception initialized with the text `Invalid rating`.

* Implement the `>` operator (`__gt__`) in the class, which expects another film object as a parameter and returns a boolean value. The operator should return true exactly when the current film is longer than the film received as a parameter (`length` attribute).

* Override the function that converts to string so that the film’s data is returned in the following format: `{title}, {length} minutes long film, with {number_of_ratings} ratings.`, where `number_of_ratings` is the length of the `ratings` list.

* Override the equality operator. The operator should return true exactly when all attributes of the two films being compared match in order.