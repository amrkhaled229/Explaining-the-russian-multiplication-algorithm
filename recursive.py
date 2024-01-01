def RusseRec(n, m):
    if n % 2 == 0:
        return RusseRec(n // 2, 2 * m)
    elif n == 1:
        return m
    else:
        return RusseRec((n - 1) // 2, 2 * m) + m
