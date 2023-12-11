### Example

Input.

```python
param = {
    'apple': 'fruit',
    'pear': 'fruit',
    1: 12,
    3: 23,
    5: 23,
    4: True,
    3.14: 'number',
    6.42: True
}
```

Output.

```python
output = {
    'fruit': ['apple', 'pear'],
    12: [1],
    23: [3, 5],
    True: [4, 6.42],
    'number': [3.14]
}
```