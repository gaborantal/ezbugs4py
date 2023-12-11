# Example

```python
k1 = Basket("wood", 15)
print(k1)
# The wood basket size is 15, currently there are 0 candies in it

k1.add_candy("apple")
print(k1)
# The wood basket size is 15, currently there are 1 candies in it

k1.size = 0
print(k1)
# The wood basket size is 0, currently there are 0 candies in it

k2 = Basket("plastic", 3)
k2.add_candy("cherry")

print(k1 + k2)
# The mixed material basket size is 3, currently there are 1 candies in it

print(k1 == k2)
# False
```