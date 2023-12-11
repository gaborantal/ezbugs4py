def k_combination(n, k):
    if not isinstance(n, int) or not isinstance(k, int) or k > n or k <= 0:
        return 0

    def factor(n):
        f = 1
        for k in range(2, n + 1):
            f *= k
        return f

    return factor(n) / (factor(k) * (factor(n - k)))
