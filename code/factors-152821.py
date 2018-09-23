import math
def prime(data):
	prime = 0

	global prime_list

	if data == 1 or data == 0:
	        prime = 1
	else:
	        for x in range(2, int(math.sqrt(data)+1)):
	                if (data % x == 0):
	                        prime = 1
	                        break
	if prime == 0:
		prime_list.append(int(data))





if __name__ == "__main__":
	prime_list=[]
	for i in range(1000):
		prime(i)
	#print(prime_list)

	data = int(input())

	value = data
	result = []
	while value != 1:
		for i in prime_list:
			if value % i == 0:
				result.append(i)
				#print(result)
				value = int(value/i)
				break
		#print ("gg")
	
	#LD = len(result)
	for i in result:
		print(i)
	
