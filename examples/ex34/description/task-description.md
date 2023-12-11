### Point

- To create a new instance, two parameters are required, representing two coordinates (`x` and `y`).
- If the type of one parameter is not `float`, raise a `ValueError` with the following messages, respectively:
    - `Wrong X value: {x_value}, {x_type}`, where `{x_value}` is the value of the `x` parameter, and `{x_type}` is the
      string representation of its type,
    - `Wrong Y value: {y_value}, {y_type}`, where `{y_value}` is the value of the `y` parameter, and `{y_type}` is the
      string representation of its type.
- If there is no error, store the coordinates in the instance as `_x` and `_y`.
- The class should have a string representation in the following format: `P({x_value},{y_value})`, where `{x_value}`
  and `{y_value}` are the values of the coordinates passed in the parameters.
- The class has its own equality operator, which returns true only when comparing two `Point` instances, and the
  coordinates contain the same values.
