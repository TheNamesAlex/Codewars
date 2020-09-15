def find_missing_letter(chars):
    is_upper = False
    all_chars = [chr(i) for i in range(127)]
    if chars[0].isupper():
        
        is_upper = True
        all_chars = [i.upper() for i in all_chars]
        
        #drop everything befor first letter and after last letter
        all_chars = all_chars[all_chars.index(chars[0]):all_chars.index(chars[-1])+1]
        return list(set(all_chars).difference(chars))[0]
    else:
        all_chars = all_chars[all_chars.index(chars[0]):all_chars.index(chars[-1])+1]
        return list(set(all_chars).difference(chars))[0]
     