## Alliteration Check (20 pont)

Create a function named `alliteration` that expects a text consisting of multiple words separated by spaces as a parameter. The function should return the size (number of words) of the largest consecutive alliterating section in the text. (Two words alliterate if their starting letter is the same). It is important to note that lowercase and uppercase letters are not distinguished (for example, the words `master` and `Mercury` both start with the letter `m`).

If the function is called with a non-string type parameter, or the parameter is a text consisting of fewer than 2 words, then the return value should be `None`.
