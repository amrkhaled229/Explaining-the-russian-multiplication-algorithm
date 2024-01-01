def Russe(n, m):
    p = 0
    while n != 1:
        if n % 2 == 1:
            p = p + m
        n = n // 2
        m = 2 * m
    return p + m
