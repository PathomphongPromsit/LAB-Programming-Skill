def radix (base,data):
	ten = 0
	LD = len(data[0])
	for i in range(LD):
		if i != LD-1:
			ten = (ten+data[0][i])*base
		else:
			ten = ten+data[0][i]
	print(ten)



if __name__ == "__main__":

	data_test = int(input())
	for i in range(data_test):
		base = int(input())
		data =  [[int(i) for i in input()] for j in range(1)]
		radix(base,data)
