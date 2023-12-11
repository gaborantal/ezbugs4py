## Example

```
#p1 = Point(1,1.1) # Wrong X value: 1, <class 'int'>
#p1 = Point(1.1,1) # Wrong Y value: 1, <class 'int'>
p1 = Point(1.1, 2.2)
print(p1) # P(1.1,2.2)
p2 = Point(1.1, 2.2)
print(p1 == p2) # True

```