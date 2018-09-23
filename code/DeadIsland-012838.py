w,h = [int(i) for i in input().split()]

matrix = [[int(j) for j in input().split()] for k in range(h)]
chk =0


for m in range(h):
	for n in range(w):
		#print(m,n,matrix[m][n])

# 		#   xxx
# 		#	xxx
# 		#	xxx
		try:   
			OL =  matrix[m-1][n-1]                           
		except IndexError:
			OL = 0
		try:                              
			O =  matrix[m-1][n]
		except IndexError:
			O = 0
		try:                              
			OR =  matrix[m-1][n+1]
		except IndexError:
			OR=0
		try:                              
			L =  matrix[m][n-1]
		except IndexError:
			L=0
		try:                              
			R =  matrix[m][n+1]
		except IndexError:
			R=0
		try:                              
			UL =  matrix[m+1][n-1]
		except IndexError:
			UL=0
		try:                              
			U =  matrix[m+1][n]     
		except IndexError:
			U=0
		try:                              
			UR =  matrix[m+1][n+1]  
		except IndexError:
			UR=0
		                          
			

		value = matrix[m][n]
			
		if value == 1 and OL+O+OR+L+R+UL+U+UR <2:
				
				chk =1
				break 
if chk ==0:
	print("Yes")
else:
	print("No")
