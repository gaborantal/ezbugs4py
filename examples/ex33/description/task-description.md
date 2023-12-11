## Swap Function

Create a function called `swap` that takes 2 parameters! The first one is a string, and the second one is a dictionary.
The function returns a string.

The function swaps the words in the first parameter following these rules:

- Splits the string into a list of words along spaces,
- Converts each word to lowercase,
- Does not change the order of the words,
- Replaces accented characters (`çéïàôñā`) with their unaccented counterparts,
- Searches for keys in the dictionary within the list of words and, if there is an exact match, replaces the word with
  the value associated with the key,
- Removes words from the list that are a maximum of 3 characters long,
- Separates each word with a single minus sign.

The function returns the modified string.

