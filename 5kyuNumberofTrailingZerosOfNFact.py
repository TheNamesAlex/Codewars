def zeros(n):
    from scipy.special import factorial
    import numpy as np
    
    count = 0

    i=5
    while (n/i>=1): 
        count += int(n/i) 
        i *= 5
  
    return int(count) 