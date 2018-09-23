def sentValue(matrix, n, m):
    var = True
    for i in range(n):
        for j in range(m):
            value = matrix[i][j]  #any value in matrix
            if splitRowCol(matrix, value, i, j, n, m): # cal can't cut R C /value[ij]
                var = False
                return var
                
            
    return var
 ########################################################################################## 
def splitRowCol(matrix, value, i, j, n, m):
    row = [matrix[i][x] for x in range(m) if x != j]  # row of value i j
    col = [matrix[x][j] for x in range(n) if x != i]  # col of value i j
    R= canCut(value, row)
    C= canCut(value, col)
    result = R and C
    return result # >= aij  cat't cut any line
##########################################################################################
def canCut(value, line):
    cut = False
    for item in line:  
       if value < item: #can't cut
           cut = True
           return cut
    return cut
###########################################################################################
if __name__ == '__main__':
    n, m = [int(i) for i in input().split()]  #input size
    if m == 1 or n == 1:
    	print ("YES")
    else:
	    matrix = [[int(j) for j in input().split()] for i in range(n)] #insert data into matrix
	    if sentValue(matrix, n, m): #call fn test any value in matrix
	        print ("YES")
	    else:
	        print ("NO")
