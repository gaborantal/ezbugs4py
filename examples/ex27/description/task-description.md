Write a function named `split` that expects a text and a list of integers as parameters.
The function's task is to break down the received text into subtexts consisting of an appropriate number of words.
The number of words in the subtexts is given by the list containing the integer values. **See example!**
The function should return the list of subtexts obtained in this way.
If the text consists of more words than the number list has, then the last element of the result list contains the
remaining text.
If the text consists of fewer words than the number list has, then the result list should be empty.
It should not be necessary to provide the number list, in this case, the result list should contain one element, which
contains the entire text.
