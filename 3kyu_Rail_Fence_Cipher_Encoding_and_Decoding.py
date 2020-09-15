def encode_rail_fence_cipher(string, n):
    rails = {}
    k = 0
    
    levels = [i for i in range(n-1)]+[i for i in range(n-1,0,-1)]
    levels = len(string)*levels
    
    for char in string:
        level = levels[k]
        if level in rails.keys():
            rails[level].append(char)
        else:
            rails[level] = [char]
        k+=1
    result = ''
    for level in rails.keys():
        for char in rails[level]:
            result += char
    return result

def decode_rail_fence_cipher(string, n):
    ## get lengths of levels, same as above
    import numpy as np
    rails = {}
    steps = {}
    k = 0
    
    levels = [i for i in range(n-1)]+[i for i in range(n-1,0,-1)]
    levels = len(string)*levels
    
    for char in string:
        level = levels[k]
        if level in rails.keys():
            rails[level].append(char)
        else:
            rails[level] = [char]
        k+=1
        
    #for level in rails.keys():
    #    rails[level] = len(rails[level])
    
    # for each level, we find which indices of the initial string are held at what position
    for level in rails.keys():
        
        # define step sizes for each level --> e.g. for n = 3:    level 1 holds indices 0,4,8,12,....+4+4+4
        #                                                         level 2 holds indices 1,3,5,7,9,...+2+2+2+2
        #                                                         level 3 holds indices 2,6,10,14,...+4+4+4+4
        
        #alternating step sizes s1 and s2 for each level
        s1 = 2*(n-level-1)
        s2 = 2*(n-1) - s1
        
        #using cumsum, we form the complete index vectors for the result
        steps[level] = [(s1,s2) for i in range(len(string)*n)]
        steps[level] = [level] + [item for t in steps[level] for item in t] 
        steps[level] = np.sort(list(set(np.cumsum(steps[level]))))
        steps[level] = steps[level][steps[level]<len(string)]  
    
    result = ['' for i in range(len(string))]
    
    lvl = 0
    k = 0
    counter = 0
    
    #for each level in the ciphered string, we expand the string to the corresponding results indices
    #and head on to the next level
    
    for level in steps.keys():
        idx = steps[level]
        for i in idx:
            result[i] = string[k]
            k+=1

    return ''.join(result)