def set_bug(col,low,bugs):
	col = int(col)
	low = int(low)
	global matrix,count
	matrix[col][low] = "p" 
	count -=1
	
	for i in range(col-bugs,col+bugs+1):
		for j in range(low-bugs,low+bugs+1):
			#print(i,j)
			if i>=0 and j >=0:
				try:  
					data = matrix[i][j]                        
					if data ==0:
						matrix[i][j] = "p" 
						count-=1     
				except IndexError:
					pass
					
	# for ll in range(n):
	# 	print(matrix[ll])
	# print()
if __name__ == "__main__":
	#set_bug(4,3,2)
	n = int(input())
	count = n*n
	matrix = [[int(i) for i in input().split()]for j in range(n)]
	for k in range(n):
		for l in range(n):
			if matrix[k][l] != 0 and matrix[k][l] != "p":
				bugs = matrix[k][l]
				set_bug(k,l,bugs)
	print(count)

	
