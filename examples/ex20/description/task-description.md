## Task 1: Word Statistics

Write a function named `word_statistics` that takes a multi-word text as a parameter (the words are separated by spaces)! The function should determine:

* ...how many words are in the text
* ...the average length of the words in characters (the sum of the lengths of the words divided by the number of words) - convert the obtained average to an integer
* ...how many words in the text are longer than the previously calculated average word length!

The result should be returned in a dictionary in the following format:

```python
{
  'word_count': NUMBER_OF_WORDS_IN_THE_TEXT,
  'average_length': AVERAGE_LENGTH_OF_WORDS_AS_AN_INTEGER,
  'long_words': NUMBER_OF_WORDS_LONGER_THAN_THE_AVERAGE
}
```

If the function receives a non-text type parameter, or the text provided in the parameter is shorter than 2 words, then the return value should be an empty dictionary!
