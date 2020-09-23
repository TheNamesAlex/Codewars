def recoverSecret(triplets):
    all_letters = list(set([i for triplet in triplets for i in triplet]))
    
    for triplet in triplets:
    
        if all_letters.index(triplet[1])>all_letters.index(triplet[2]):
            all_letters.remove(triplet[1])
            all_letters.insert(all_letters.index(triplet[2]), triplet[1])
        if all_letters.index(triplet[0])>all_letters.index(triplet[1]):
            all_letters.remove(triplet[0])
            all_letters.insert(all_letters.index(triplet[1]), triplet[0])
            
    for triplet in triplets:
    
        if all_letters.index(triplet[1])>all_letters.index(triplet[2]):
            all_letters.remove(triplet[1])
            all_letters.insert(all_letters.index(triplet[2]), triplet[1])
        if all_letters.index(triplet[0])>all_letters.index(triplet[1]):
            all_letters.remove(triplet[0])
            all_letters.insert(all_letters.index(triplet[1]), triplet[0])
    
    return ''.join(all_letters)