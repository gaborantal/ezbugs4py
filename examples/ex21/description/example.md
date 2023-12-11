# Example

```python
course1 = Course('Approximate and Symbolic Calculations')
course1.course_code = 'IB370G-12'
course1 += ['ASD123', 'F00B4R', 'ASD123', 'NEP4LF']

course2 = Course('Approximate and Symbolic Calculations', 'ib110g-1')
course2 += ['ASD123', 'F00B4R', 'ASD123', 'NEP4LF']

print(course2.course_code)               # 'IB370G-12'
print(course2)                           # 'Approximate and Symbolic Calculations (code: IB110G-1)'
print(course2.list_students())           # 'ASD123, F00B4R, NEP4LF'

print(course1 == course2)                # True
print(course1 == 'cat')                  # False
```
