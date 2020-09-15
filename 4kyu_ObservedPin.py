def get_pins(observed):
    import itertools
    observed = [str(i) for i in observed]
    
    ones = ['124']
    twos = ['1235']
    threes = ['236']
    fours = ['1457']
    fives = ['24658']
    sixes = ['3569']
    sevens = ['478']
    eights = ['78509']
    nines = ['896']
    zeros = ['08']
    
    ones = [str(num) for num in ones[0]]
    twos = [str(num) for num in twos[0]]
    threes = [str(num) for num in threes[0]]
    fours = [str(num) for num in fours[0]]
    fives = [str(num) for num in fives[0]]
    sixes = [str(num) for num in sixes[0]]
    sevens = [str(num) for num in sevens[0]]
    eights = [str(num) for num in eights[0]]
    nines = [str(num) for num in nines[0]]
    zeros = [str(num) for num in zeros[0]]
    
    lookup = {'1':ones,'2':twos,'3':threes,'4':fours,'5':fives,'6':sixes,'7':sevens,'8':eights,'9':nines,'0':zeros}
    #print(lookup)
    
    combinations=[]
    
    for char in observed:
        combinations.append(lookup[char])
    #print(combinations)
    
    keys = []
    for element in itertools.product(*combinations):
        key = ''.join(list(element))
        keys.append(key)    
    #print(ones)
    return keys