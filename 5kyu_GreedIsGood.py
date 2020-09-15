def score(dice):
    ones = dice.count(1)
    sixes = dice.count(6)
    fives = dice.count(5)
    fours = dice.count(4)
    threes = dice.count(3)
    twos = dice.count(2)
    res = (ones // 3)*1000+(ones % 3)*100 + (fives // 3)*500+(fives % 3)*50 + (sixes // 3)*600 + (fours // 3)*400 + (threes // 3)*300 + (twos // 3)*200
    #print(dice)
    #print(res)
    return res
   