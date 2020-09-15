def longest(s1, s2):
    res = s1+s2
    res = [char for char in res]
    res = sorted(list(set(res)))
    result = ''
    for i in res:
        result +=i
    return result