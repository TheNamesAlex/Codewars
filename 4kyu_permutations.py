def permutations(string):
    from itertools import permutations
    #for x in permutations(string):
    #    print(x[0])
    return sorted(set([''.join(list(x)) for x in permutations(string)]))