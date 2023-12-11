### Example

```
pp = PrettyPrint("[pp]")
print(pp.get(None))
print(pp.get(1))
print(pp.get(2.2))
print(pp.get("eee"))
pp.prefix = ["abc", "def"]
print(pp.get([4,3,2]))
print(pp.get({"abc":3, "erq":"xx"}))
print(pp.get(Exception("err")))
```

Output:

```
[pp] None
[pp] (integer) 1
[pp] (float) 2.2
[pp] (string) eee
['abc', 'def'] (list object) [4, 3, 2]
['abc', 'def'] (dictionary) {'abc': 3, 'erq': 'xx'}
['abc', 'def'] (unknown) err
```
