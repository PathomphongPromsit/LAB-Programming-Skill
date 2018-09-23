
if __name__ == "__main__":
	M, N = [int(i) for i in input().split()]
	deep_port =[]
	for j in range(M):
		deep_port.append(int(input()))
	#print(deep_port)
	boat = []
	for k in range(N):
		boat.append(int(input()))

	deep_port.sort()
	boat.sort()

	stop_port = -M
	stop_boat = -N
	pointer_one = -1
	pointer_two = -1

	count = 0
	while pointer_one >= stop_port and pointer_two >= stop_boat:
		if deep_port[pointer_one]>=boat[pointer_two]:
			pointer_one-=1
			pointer_two-=1
			count+=1
		else:
			pointer_two -=1
	print(count)

