def get_sum(a,b):
    if a == b:
        return a
    elif a<b:
        return sum([i for i in range(a,b+1)])
    else:
        return sum([i for i in range(b,a+1)])
        