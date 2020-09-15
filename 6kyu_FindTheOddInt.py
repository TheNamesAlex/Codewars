def find_it(seq):
    counts = {}
    for num in seq:
        if num in counts.keys():
            counts[num] +=1
        else:
            counts[num] = 1
    
    for key in counts.keys():
        if counts[key] % 2 == 1:
            return key