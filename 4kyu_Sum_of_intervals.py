def sum_of_intervals(intervals):
    import numpy as np
    from operator import itemgetter
    
    #shift all entries to right half plane
    intervals = [(tuple[0]-min(intervals,key=itemgetter(0))[0]+1,tuple[1]-min(intervals,key=itemgetter(0))[0]+1) for tuple in list(intervals)]#list(intervals)
    n_x = len(intervals)
    n_b = max(intervals,key=itemgetter(1))[1]
    arr = np.zeros((n_x,n_b))
    
    for row, interval in enumerate(intervals):
        a,b = interval
        arr[row, a:b] = 1
    
    #orthogonal projection onto single row vector
    proj = np.ones((1,n_x))
    return np.sum(sum(proj@arr >= 1))  