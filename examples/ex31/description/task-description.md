- Write a class named `Basket` that will represent a basket storing candies! The class should have 3 data
  members: `material`, `_size`, and a list named `candies`, which contains the candies (i.e., their flavors) in the
  basket.*

- The constructor receives the material of the basket and its size as parameters (in this order), and initializes
  the `material` and `_size` data members based on these! The `candies` data member should be initialized with an empty
  list!

    - The `_size` parameter value should not be mandatory, its default value should be 10!

- Create a get and set property for the `_size` data member, named `size`!

    - The getter should return the value of the data member.
    - The setter should set the value of the data member, and also check whether the number of candies in the basket
      exceeds the new size of the basket. If so, then cut off the end of the candies list so that the list is at most as
      long as the size. For example, in the case of a list of 5 elements, if we set the size to 3, we should remove the
      last two elements of the list.

- Override the method responsible for converting the object to text so that it returns a text in the following
  format: `The {material} basket size is {size}, currently there are {number of candies} candies in it` (
  where `number of candies` is the length of the `candies` list).

- Implement the `add_candy` method, which receives a candy (i.e., the flavor of the candy, text) as a parameter!

    - If no more candies can fit in the basket (the size data member tells us this), then throw a `ValueError`
      exception, which you initialize with the text `The basket is full`!
    - Otherwise, check if there is already a candy with the same flavor in the candies list!
        - If not, simply add the candy to the list!
        - If there is, throw a `ValueError` exception, initialized with the text `This candy is already in the basket`.

- Override the `+` operator (`__add__`), which expects another basket object as a parameter. The operator should set the
  new basket's material data member to `mixed material`, and its size to the sum of the sizes of the two baskets. The
  new basket should contain all the candies of both baskets.

- Override the equality-checking operator! The operator should return true exactly when the material and size of the
  baskets to be compared match. Don't worry about anything else.
