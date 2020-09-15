def tribonacci(signature, n):
    result = signature
    if n <=2:
        return(result[:n])
    else:
        for i in range(3,n):
            result.append(sum(result[i-3:i]))
    return result   