Write a function named `dict_complete` that takes a dictionary as a parameter. In the dictionary, the keys are integers starting from 1 (1, 2, 3, etc.), but unfortunately, some of them are missing. The function should complete the dictionary by inserting the missing keys (between 1 and the maximum key) with a value of 0 into the data structure.

If the dictionary received as a parameter is empty, then the return value of the function should also be an empty dictionary.
It is not guaranteed that the keys appear in ascending order, so the last key is not necessarily the maximum (see: second example)!
