def helper(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = helper(n // 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)

def fib(n):
    if n <= -1:
        return helper(-n)[0]*(-1)**(-n+1)    
    return helper(n)[0]