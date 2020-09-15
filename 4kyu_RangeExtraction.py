def solution(args):
    res = ''
    beginning = 0
    end = 0
    k = 0
    while k < len(args):
        beginning = args[k]
        while (k < len(args)-1) and (args[k]+1 == args[k+1]): 
            k+=1
            
        end = args[k]
        if end - beginning >=2:
            res += str(beginning)+'-'+str(end)+','
        elif end - beginning ==1:
            res += str(beginning)+','+str(end)+ ','
        else:
            res += str(beginning)+','
        k+=1
            
    return res[:-1]             