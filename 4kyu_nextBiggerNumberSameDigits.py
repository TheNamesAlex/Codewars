def next_bigger(n):
    import numpy as np
    digits = [i for i in str(n)]
    n_digits = len(str(n))
    is_desc = True
    #we identify the left part and the anchor, i.e. the first non ascending number from the right 
    for i in range(n_digits-1,0,-1):
        if digits[i] > digits[i-1]:
            anchor = digits[i-1]
            is_desc = False
            break
    
    if is_desc:
        return -1
    if len(str(n)) == 0:
        return -1
    
    #we separate the left, untouched part and find the new next digit 'new_anchor'
    left = digits[:i-1]
    right = np.sort(digits[i-1:])
    
    #find index of old anchor and go one step further from that index to extract new anchor
    idx = int(np.ravel(np.where(right>anchor))[0])

    new_anchor = right[idx]
    new_right = np.delete(right, idx)
    res = int(''.join(left) + str(new_anchor) + ''.join(new_right))
    #print(n, res)
    return res
