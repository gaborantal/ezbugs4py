# Example

```python
    t1 = Cemetery("MainCemetery", 400)
t2 = Cemetery("OtherCemetery", 5)

t1.number_of_graves = 3
print(t1.number_of_graves)  # 10

t1 += "Albert"
t1 += "Bela"
t1 += "Bela"
print(t1.ghosts)  # ['Albert', 'Bela1', 'Bela2']
print(t1)  # In the MainCemetery cemetery, there are 10 graves, and 3 ghosts haunt it

try:
    t1 += 666
except ValueError as ve:
    print(ve)  # Not a ghost

print(t1 == t2)  # False
```