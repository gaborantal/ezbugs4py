# Example

```python
    t1 = HauntedHouse("Apple Street 15.", 400)
t2 = HauntedHouse("Banana Street 20.", 5)

t1.number_of_cats = 3
print(t1.number_of_cats)  # 10

t1 += "Albert"
t1 += "Bela"
t1 += "Bela"
print(t1.ghosts)
# ['Albert', 'Bela1', 'Bela2']
print(t1)
# The haunted house at Apple Street 15. has 10 cats, and 3 ghosts haunt it

try:
    t1 += 666
except ValueError as ve:
    print(ve)  # Not a ghost

print(t1 == t2)  # False
```