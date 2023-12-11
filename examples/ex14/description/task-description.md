## Clustering

Cluster analysis is a procedure that allows us to group elements, classifying them. These groups are called clusters.
The data within each cluster are similar to each other based on some property, and differ from the elements of other
clusters along this property.

Create a class named `Clustering` that represents clustering, derived from the `dict` type. The class represents
clustering, storing element-cluster pairs. The following should be true for the class.

+ If not specified otherwise, throw a `TypeError` exception when passing an inappropriate type of parameter.
+ Create a constructor that expects a single string parameter for the name of the clustering algorithm. Store the
  algorithm's name in the `_algorithm` attribute.
+ Create a read-only property for the `_algorithm` attribute that returns it in the following format: `_algorithm = "
  k-neighbor"` then the return value is `"k-neighbor" algorithm`.
+ Create a two-parameter `put_into` method that places the given element into the specified cluster. The first parameter
  is the element (either int or str); the second parameter is the name of the cluster (can only be of string type). If
  the element has not been placed in any cluster yet, add it to the internal dictionary, with the element as the key and
  the cluster name as the value. If the element is already in some cluster, move it to the new cluster. The method
  should return `True` if a new element has been added and `False` if the existing element's cluster has been modified.
+ Create a read-only `cluster_count` property that returns the number of different clusters stored in the class. For
  example: `{'apple': 'fruit', 'pear': 'fruit', 'carrot': 'vegetable'}`, the count is `2` (fruit and vegetable).
+ Create a one-parameter method named `count_of` that takes a string and returns the number of elements belonging to the
  specified cluster. If a cluster name is given that does not exist in the class, return `0`. For example: In case of
  `{'apple': 'fruit', 'pear': 'fruit', 'carrot': 'vegetable'}`, `count_of('fruit') = 2` (apple and pear),
  and `count_of('mushroom') = 0`.
+ To implement `cluster_count` and `count_of`, you can use the function created in the previous task, but it is not
  mandatory and does not earn extra points.
+ Override the class's string representation. The textual representation of the class should follow this pattern: "N
  items in `cluster_count` clusters detected with `algorithm`", where N is the total number of clustered elements.
