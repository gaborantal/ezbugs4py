## Surreal Numbers

The surreal number is a theoretical mathematical construction. Every surreal number consists of two sets: left and
right. The only condition for these two sets is that every element in the left set (L) must be smaller than every
element in the right set (R). The sets can be empty ({}) or contain any surreal numbers. **If either set is empty, it is
true that every element in the left set is smaller than every element in the right set (even with 0 elements).**

Create a class named `SurrealNumber` representing a surreal number. The class should adhere to the following:

+ If a method receives an improper type and is not specified otherwise, it should return None.
+ Create a constructor that takes two sets (`set()`) as parameters (`left` and `right`) and uses them to populate the
  class's private (`_left` and `_right`) attributes. Place only surreal numbers in the two sets, disregarding any other
  elements. If either parameter is not a set, raise a TypeError exception without a message.
+ The class should have two attributes defining the two sets of the number (`_left` and `_right`). Define a getter
  (read-only property) for each attribute, which returns the sets as tuples.
+ Override the string representation of the class to return the numbers in the following format (no spaces around any
  character):
  {`left` set elements separated by commas|`right` set elements separated by commas}, examples:
    + left = {} right = {} in this case: `{|}`
    + left = {s1, s2, ...} right = {} in this case: `{s1,s2,...|}`
    + left = {s1, s2, ...} right = {s1, s4, s5, ...} in this case: `{s1,s2,...|s1,s4,s5,...}`
+ Override the less-than-or-equal-to (`a <= b`) operator (`__le__(a, b)`). A The operator should only compare surreal
  numbers. Two numbers (a and b) are **false** for a <= b if
    + there is an element in a.left that is less than or equal to b (b <= a.left) **or**
    + there is an element in b.right that is less than or equal to a (b.right <= a).
+ Override the less-than (`a < b`) operator (`__lt__(a, b)`). The operator should only compare surreal numbers. Two
  numbers (a and b) are true for a < b if it is not true that b <= a.
+ Create a parameterless `check` method that checks if it is true for the number that every element in L must be smaller
  than every element in R. If true, return `True`; otherwise, return `False`.
