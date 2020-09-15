def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    rt = sq**0.5
    if rt % 1 == 0:
        return (rt+1)**2
    else:
        return -1
        
