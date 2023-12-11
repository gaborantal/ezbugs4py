- Write a class named `Cemetery` that represents a cemetery haunted by ghosts! The class should have 3 data
  members: `name`, `_number_of_graves`, and a list named `ghosts` that stores the ghosts haunting the cemetery!

- The constructor receives the name of the cemetery and the number of graves as parameters (in this order), and
  initializes the `name` and `_number_of_graves` data members based on these! The `ghosts` data member should be
  initialized with an empty list!

    - It should not be mandatory to provide the value of the `_number_of_graves` parameter, its default value should be
      10!

- Create a get and set property for the `_number_of_graves` data member, named `number_of_graves`! The getter should
  return the value of the data member, the setter should check that the new value is a number greater than or equal to
  10!

    - If the value of the parameter in the setter is appropriate, then set the data member to the value received in the
      parameter!
    - In case of an incorrect value, the setter should set the value of the data member to 10!

- Rewrite the class constructor so that the value of `_number_of_graves` is also checked here!

- Override the method responsible for converting the object to text so that it returns a text in the following
  format: `In the {name} cemetery, there are {_number_of_graves} graves, and {number of ghosts} ghosts haunt it` (
  where `number of ghosts` is the length of the `ghosts` list).
  If no ghost haunts the cemetery, then the result should be the
  text `In the {name} cemetery, there are {_number_of_graves} graves, and no ghosts haunt it`.

- Override the `+=` operator (`__iadd__` method) in the class, which receives a ghost (i.e., the name of the ghost,
  text) as a parameter!

    - If the parameter is not of string type, throw a `ValueError` exception, initialized with the text `Not a ghost`!

    - Otherwise, look in the list to see if there is already a ghost with the same name!
        - If not, simply add the ghost to the list!
        - If there is, append a `1` to the end of the name of the identical ghost in the list, and a `2` to the name of
          the ghost received in the parameter, and add it to the list in this way.

- Override the equality-checking operator! The operator should return true exactly when the names of the cemeteries to
  be compared and the number of their graves match. Don't worry about anything else.

