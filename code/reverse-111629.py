from __future__ import print_function
def reverse(string_list,start_index,stop_index):
	start_index -= 1
	stop_index -= 1
	reverse_list = string_list[start_index:stop_index+1]
	LRevese= len(reverse_list)
	for i in range(1,LRevese+1):
		string_list[start_index] = reverse_list[-i]
		start_index += 1
	return string_list


if __name__ == "__main__":
	n = int(input())
	for i in range(n):
		string = input()
		string_list = list(string)
		operand = int(input())
		for i in range(operand):
			start_index,stop_index = [int(i) for i in input().split()]
			reverse(string_list,start_index,stop_index)
		for i in string_list:
 			print(i, end='')
		print()

