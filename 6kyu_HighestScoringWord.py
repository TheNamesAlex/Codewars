def high(x):
    import string
    word_value=[]
    for word in x.split(' '):
        value = 0
        for char in word:
            value += string.ascii_lowercase.index(char)
        word_value.append((word,value))
    
    
    return sorted(word_value,reverse =True, key=lambda x: (x[1],x[0]) )[0][0]