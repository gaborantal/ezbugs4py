def split(text, nums):
    res = list()
    words = text.split(' ')
    for num in nums:
        part = words[0:num]
        res.append(part)
        words = words[num:]
    if len(words) > 0:
        res.append(words)
    print(res)
