def disemvowel(string):
    dropped = ['a','e','i','o','u','A','E','I','O','U']
    for i in dropped:
        string = string.replace(i,'')
    return string