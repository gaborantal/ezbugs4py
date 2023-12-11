## Selection

Write a function called `filter` that takes a single parameter, which is a text. In the text, words are separated by
commas (`,`). The function should return a list with the following criteria:

* Words that are **longer** than the average length of words in the input text should be **reversed**.
* Words in the list should also be **capitalized**.
* The **order** of words in the list should **remain the same** as in the input.

If the function receives a parameter that is not of string type, or the text in the parameter is an empty string (text
of length 0), then the return value should be an **empty list**!
