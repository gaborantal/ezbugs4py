- Create a class named `Hypercube` that is intended to represent a hypercube.
- The class expects the "cube" dimension and side length in its constructor.
    * These values are stored in the private `_dimension` and `_length` data members, respectively.
    * Create working `dimension` and `length` property getters and setters for these.
    * If any parameter is less than zero, the constructor should throw a general exception with the text: `Wrong Hypercube!`
    * If any setter parameter is less than zero, the setter should throw a general exception with the text: `Wrong Hypercube!`
- Create a `get_no_vertex` query member function that returns the number of points of the hypercube. The following formula can be used: `2^dimension`. If it cannot be calculated, return 0.
- Create a `get_no_edge` query member function that returns the number of edges of the hypercube. The following formula can be used: `dimension * 2^(dimension-1)`. If it cannot be calculated, return 0.
- Create a `get_no_face` query member function that returns the number of faces of the hypercube. The following formula can be used: `2^(dimension-2)*(dimension! / (2*(dimension-2)!))`. If it cannot be calculated, return 0. (**hint**: implement the factorial with a helper function: `n! = 1 * 2 * .. (n-1) * n`)
- Create a `get_area` query member function that returns the "hyper-volume" of the hypercube. The following formula can be used: `side_length^dimension`. If it cannot be calculated, return 0.
- Override the equality-checking operator. The operator should return true exactly when all parameters of the two Hypercubes to be compared are equal.
- Override the function that implements the conversion to text, which should return the following text: `Dim: {dimension}, Len: {side_length}, Area: {hyper-volume}`, where `{dimension}` and `{side_length}` are the parameters given during construction, and `{hyper-volume}` is the "hyper-volume" value returned by the query function.