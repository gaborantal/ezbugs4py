Create a class named `Mathematician` that has 3 data members: `_name`, `favorite_length`, and a dictionary
named `studies`.

The constructor receives the name and favorite length as parameters (in this order), and initializes the `_name`
and `favorite_length` data members with these. The favorite length should not be mandatory, its default value should be
3. The `studies` data member should be initialized with an empty dictionary.

Create a get and set property for the `_name` data member, named `name`. The getter should return the value of the data
member, the setter should set the value of the data member to the value received in the parameter, if it is of string
type. In case of a different type, the setter should do nothing.

Write a `add_study` method that expects a list filled with integers as a parameter. Depending on the values of the list,
do the following:

* If the numbers in the list have the same length, and this length is exactly the current favorite length of the
  mathematician, add the study to the studies dictionary with the favorite_length key
* If the numbers in the list have the same length, but this length differs from the favorite length, update the favorite
  length to the length of the numbers in the list
* In all other cases, the received numbers are incorrect

In case of incorrect numbers, throw a `ValueError` exception, which you initialize with the text `Ugly numbers`.

Implement the `<` operator (`__lt__`) in the class, which expects another Mathematician object as a parameter, and
returns a logical value. The operator should return true exactly when the current mathematician's favorite length is
less than the favorite length (`favorite_length` data member) of the mathematician arriving in the parameter.

Override the function implementing the conversion to text so that it returns the data of the mathematician in the
following
form: `The mathematician named {name} has a favorite number length of {favorite_length}, and participated in {study_number} studies.`,
where `study_number` is the number of values stored in `studies`.