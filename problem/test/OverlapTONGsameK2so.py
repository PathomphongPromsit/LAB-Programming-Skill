def creat_matrix(i,a,b):
	m=[]
	for k in range(a,b):
		m.append(k)
	MATRIX[i]= m
if __name__ == "__main__":
	N = int(input())
	
	MATRIX = [0 for i in range(N)]
	count = 0
	for i in range(N):
		a,b = [int(j) for j in input().split()]
		creat_matrix(i,a,b)
	MATRIX.sort()
	k = max(MATRIX[N-1])
	TEST=[0 for j in range(k+1)]
	for i in range(N-1):
		for j in range(N):
			for k in range(len(MATRIX[i])):
				if i<j:

					if MATRIX[i][k] in MATRIX[j]:
						gg = MATRIX[i][k] 
						TEST[gg]+=1

	Max =0
	index_Max =0
	for i in range (len(TEST)):
		if TEST[i] > Max:
			Max=TEST[i]
			index_Max = i
	print (index_Max)