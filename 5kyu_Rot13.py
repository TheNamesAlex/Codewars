def rot13(message):
    
    import string
    init = string.ascii_lowercase 
    c = string.ascii_lowercase 
    c = c[13:]+c[:13]
    
    sub = dict(zip(init,c))
    for m in message:
        if m.lower() not in sub.keys():
            sub[m] = m
    
    res = ''
    for char in message:
        if char.isupper():
            res+=sub[char.lower()].upper()
        else:
            res+=sub[char]
            
    return res