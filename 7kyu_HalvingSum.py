def halving_sum(n): 
    # your code here
    # create list of all halves
    halves = []
    while n>=1:
        halves.append(n)
        n = n//2
    return sum(halves)