def get_primes(n):
    import numpy as np
    n = np.abs(n)
    primes = []
    
    while n % 2 == 0: 
        primes.append(2) 
        n = n / 2
          
    for i in range(3,int(np.sqrt(n))+1,2): 
          
        while n % i== 0: 
            primes.append(i)
            n = n / i        
    if n > 2: 
        primes.append(n)

    return [int(prime) for prime in primes]

def sum_for_list(lst):
    all_primes = {}
    set_primes = []
    
    for n in lst:   
        all_primes[n] = get_primes(n)
        set_primes += all_primes[n]
    
    set_primes = list(set(set_primes))
    res = []
    
    for prime in set_primes:
        c = 0
        for key in all_primes.keys():
            if prime in all_primes[key]:
                c += int(key)*lst.count(key)
        res.append([prime,c])

    return sorted(res, key=lambda x: x[0])