def n_grammer(s, n=3):
    res = list()
    while s:
        if len(s) > n:
            res.append(int(s[n:]))
            s = s[n:]
        else:
            s += '0' * (n - len(s))
            res.append(int(s))
            break
    return res
