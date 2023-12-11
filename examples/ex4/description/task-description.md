* Create a class named `LightString` that has 2 data members: `length` (integer) and `_lights` (list).

* The constructor receives the length and the lights as parameters (in this order), and initializes the `length` and `_lights` data members with these. When setting the lights list, use the property created below! Neither value should be mandatory, by default the length should be 0, and the lights should be an empty list.

* Create a get and set property for the `_lights` data member, named `lights`. The getter should return a copy of the data member, and the setter should set the data member to a copy of the list received as a parameter. In case of a different type, the setter should throw a `TypeError` exception with the text `The lights can only be a list!`.

* Write a `add_light` method that expects a string as a parameter. If the received value is one of the `cold_white, warm_white, red, green, blue, yellow` colors, then the function should add it to the end of the `_lights` list, otherwise it should do nothing.

* Implement the `<` operator (`__lt__`) in the class, which expects another light string object as a parameter, and returns a logical value. The operator should return true exactly when the light string is shorter than the one received as a parameter.

* Override the function that implements the conversion to text so that the light string returns its data in the following form: `{length} centimeter long light string, {number_of_lights} pieces ({different_colors}) colored lights.`, where `{different_colors}` should list the different colors found in the light string in alphabetical order, separated by commas and spaces. For example: `200 centimeter long light string, 3 pieces (blue, red, green) colored lights.`

* Override the equality-checking operator. The operator should return true exactly when all data members of the two light strings to be compared are the same in order.