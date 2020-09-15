def duplicate_encode(word):
    word = word.lower()
    counts={}
    
    for char in word:
        if char in counts.keys():
            counts[char] +=1
        else:
            counts[char] = 1
    
    return_string = ''
    
    for char in word:
        if counts[char] > 1:
            return_string += ')'
        else:
            return_string += '('
    
    return return_string