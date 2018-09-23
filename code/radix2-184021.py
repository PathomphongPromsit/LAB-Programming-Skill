from __future__ import print_function
def radix (base,data):
	value = data
	result = []
	while value != 0:
		result.append(value % base)
		value = int(value / base)
	LD = len(result)
	for i in range(LD):
		print(result[(-i)+-1],end='')
	print ()

if __name__ == "__main__":

	data_test = int(input())
	for i in range(data_test):
		data =  int(input())
		base = int(input())
		if data == 0 or base == 0:
                        print(0)
		else:
                        radix(base,data)
