## Grouping

Create a function named `groupby` that expects a dictionary as a parameter and returns another dictionary. Its task is
to group the keys of the received dictionary based on their values.

The input dictionary associates arbitrary simple types with other simple types: int, str, float, bool. Both keys and
values can store arbitrary, unknown data. The method should work for any data.

The output dictionary has keys of simple types, and its values contain lists of simple types. The keys are unique values
of the input dictionary. The values are lists of keys from the input dictionary with the given value. In the lists, the
elements occur in the appropriate number and position in the input dictionary.

If any of the input types is not appropriate, throw a `TypeException`.
