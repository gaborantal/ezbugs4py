- Write a class named `HauntedHouse` that represents a haunted house! The class should have 3 data
  members: `address`, `_number_of_cats`, and a list named `ghosts`, which stores the ghosts haunting the haunted house!
  **(3 points)**

- The constructor receives the address of the haunted house and the number of cats staying inside as parameters (in this
  order), and initializes the `address` and `_number_of_cats` data members based on these! The `ghosts` data member
  should be initialized with an empty list!

    - The `_number_of_cats` parameter value should not be mandatory, its default value should be 10! **(3 points)**

- Create a get and set property for the `_number_of_cats` data member, named `number_of_cats`! The getter should return
  the value of the data member, the setter should check that the new value is a number of 10 or more!

    - If the parameter value in the setter is appropriate, then set the data member to the value received in the
      parameter!
    - In case of incorrect value, the setter should set the value of the data member to 10! **(6 points)**

- Rewrite the class constructor so that the `_number_of_cats` value is also checked here! **(1 point)**

- Override the method responsible for converting the object to text so that it returns a text in the following
  format: `The haunted house at {address} has {_number_of_cats} cats, and {number of ghosts} ghosts haunt it` (
  where `number of ghosts` is the length of the `ghosts` list).
  If no ghost haunts the cemetery, then the result should be the
  text `The haunted house at {address} has {_number_of_cats} cats, and no ghost haunts it`. **(5 points)**

- Override the `+=` operator (`__iadd__` method) in the class, which receives a ghost (i.e., the name of the ghost,
  text) as a parameter!

    - If the parameter is not of string type, throw a `ValueError` exception, which you initialize with the
      text `Not a ghost`! **(2 points)**
    - Otherwise, look in the list to see if there is already a ghost with the same name!
        - If not, simply add the ghost to the list! **(3 points)**
        - If there is, append a `1` to the end of the name of the identical ghost in the list, and a `2` to the name of
          the ghost received in the parameter, and add it to the list in this way. **(4 points)**

- Override the equality-checking operator! The operator should return true exactly when the address of the haunted
  houses to be compared and the number of their cats match. Don't worry about anything else. **(3 points)**
