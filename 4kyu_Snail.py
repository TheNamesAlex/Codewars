def snail(snail_map):
    import numpy as np
    arr = np.array(snail_map)
    l = []
    
    if len(arr) == 0:
        return [[]]
    else:        
        try:
            while True:
                l.append(arr[0,:].tolist())
                arr = arr[1:,:]
                arr = np.rot90(arr)
        except:
            pass
        
    return([item for sublist in l for item in sublist])
    