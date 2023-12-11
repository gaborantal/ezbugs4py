## Exam

* Create a class named `Exam`, which should have a text attribute: `_subject`, and two lists of equal length: `questions` and `points`.

* The constructor should receive the subject as a parameter, which should be set as the value of the attribute using the property created below! The questions and points should be empty lists.

* reate a get and set property for the `_subject` attribute, named subject. The getter should simply return the value of the attribute. The setter, however, should check the value received as a parameter: if it is not a string, or shorter than 3 characters, it should throw a `ValueError` exception with the message `The subject must be a string at least 3 characters long!`.

* Write a method called `add_question`, which expects a question and a point value as parameters. It should check the types of the parameters, and if they are correct (string and integer), then it should append them to the end of the respective list attribute, otherwise, it should do nothing!

* Write a method called `total_points`, which does not expect any parameters, and returns the sum of the numbers in the points list!

* Implement the `+=` operator (`__iadd__`) in the class, which expects another Exam object as a parameter, and returns itself. The operator should throw a `TypeError` exception (with any message) if the other object is not of the Exam type. Otherwise, it should append the questions and their corresponding point values from the parameter Exam to its own lists, provided they are not already included.

* Override the function that converts to string so that it returns the exam data in the following format: the name of the subject, each question on a new line with the associated point value in parentheses, and at the end, on a new line, the text `Total: ` followed by the total points. The returned string should not have a newline character at the end. Example:

```
Script Languages
What is Python? (5 points)
What is an interpreter? (10 points)
Total: 15 points
```

* Override the equality operator. The operator should return true exactly when all attributes of the two exams being compared match in order.