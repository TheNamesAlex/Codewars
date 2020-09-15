def ips_between(start, end):
    no1 = start.split('.')
    no2 = end.split('.')
    
    exp = [256**(i-1) for i in range(4,0,-1)]
    
    delta = []
    result = 0
    
    for i,j in zip(no1,no2):
        delta.append(int(j)-int(i))
    for i,j in zip(delta,exp):
        result += i*j
        
    return result