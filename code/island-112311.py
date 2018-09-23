
def get_max(i, j):
	size = 2
	while True:
		#|
		for k in range(0,size):
			try:                              
				value =  matrix[i+size-1][j+k]             #see value square size
				if value == 0:
					a = size-1
					area = a*a
					return area
			except IndexError:
				a = size-1
				area = a*a
				return area

		#__
		for l in range(0,size-1):
			try:                              
				value =  matrix[i+l][j+size-1]             #see value square size
				if value == 0:
					a = size-1
					area = a*a
					return area
			except IndexError:
				a = size-1
				area = a*a
				return area
		size +=1
			
if __name__ == "__main__":
	n = int(input())
	matrix = [[int(i) for i in input()] for j in range(n)]
	x = 0
	y = 0
	area = 0
	for i in range(n):
		for j in range(n):
			if (matrix[i][j]!= 0):
				value = get_max(i,j)
				if value >  area:
					area = value
					x = i+1
					y = j+1

	print (x,y)
	print (area)




