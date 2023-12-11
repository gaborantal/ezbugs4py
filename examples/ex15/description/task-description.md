## Word length statistics

Create a function named `length_stat` that receives a text consisting of multiple words separated by spaces as a parameter. The return value of the function should be a two-element list:

* the first element of the list is the average length of the words in the text (sum of the lengths of the words / number of words), **converted to an integer type**
* the second element is the number of words in the text that are longer than the average word length.

If the function is called with a non-string type parameter, or the parameter is an empty string (0 length text), then the return value should be an empty list.
