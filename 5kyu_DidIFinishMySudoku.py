def done_or_not(board): #board[i][j]
    import numpy as np

    brd = np.array(board)
    full = [i for i in range(1,10)]

    regions_passed = False
    regions_done = 0
    
    rows_passed = False
    rows_done = 0
    
    cols_passed = False
    cols_done = 0
    
    #check regions
    for i in range(3):
        for j in range(3):
            region = brd[3*i:3*(i+1),3*j:3*(j+1)]
            sorted_values = list(sorted(np.ravel(region)))
            if sorted_values == full:
                regions_done+=1
            if regions_done==9:
                regions_passed = True
                
    #check rows            
    for i in range(9):
        row = brd[i,:]
        sorted_row = list(sorted(np.ravel(row)))
        #print(sorted_row)
        if sorted_row == full:
            rows_done+=1
        if rows_done==9:
            rows_passed = True
    
    #check cols            
    for i in range(9):
        col = brd[:,i]
        sorted_col = list(sorted(np.ravel(col)))
        #print(sorted_row)
        if sorted_col == full:
            cols_done+=1
        if cols_done==9:
            cols_passed = True
            
        
    if cols_passed and rows_passed and regions_passed:
        return 'Finished!'
    else:
        return 'Try again!'