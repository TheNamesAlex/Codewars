def iq_test(numbers):
    c = numbers.split(' ')
    num_even = 0
    num_odd = 0
    
    #first three numbers enough to determine exactly if we're looking for odd or even numbers 
    c_init = c[:3]
    for num in c_init:
        if int(num) % 2 == 0:
            num_even += 1
        else:
            num_odd +=1
            
    for idx, num in enumerate(c):
        #print(idx)
        if num_even < num_odd:
            if int(num) % 2 == 0:
                return idx+1
        else:
            if not int(num) % 2 == 0:
                return idx+1
    