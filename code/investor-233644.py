if __name__ == "__main__":
	money, n = [int(i) for i in input().split()]
	compane_list = []
	for j in range(n):
		compane_list.append(int(input()))

	compane_list.sort()		
	#print(compane_list)
	count = 0
	for k in range(n):
		if money - compane_list[k] >= 0:
			money = money -compane_list[k]
			count+=1
		else:
			break
	print(count)