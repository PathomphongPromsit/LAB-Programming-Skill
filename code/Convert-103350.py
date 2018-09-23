def int_to_binary_8bit(data):
	binary = format(data, 'b')
	digit_8 = str(binary).zfill(8)

	hbyte = digit_8[0]+digit_8[1]+digit_8[2]+digit_8[3]
	lbyte = digit_8[4]+digit_8[5]+digit_8[6]+digit_8[7]
	intHB = int(hbyte, 2)
	intLB = int(lbyte, 2)
	
	SUM = intHB+intLB
	binary_sum = format(SUM, 'b')
	
	sum_4_digit = binary_sum
	if SUM > 15:
		sum_4_digit = binary_sum[1]+binary_sum[2]+binary_sum[3]+binary_sum[4]

	sum_4_digit = str(sum_4_digit).zfill(4)
	



	redun = ""
	for i in range(4):		
		if sum_4_digit[i] == "0":
			redun += "1"
		else:
			redun += "0"
	codeword = digit_8+redun
	
	# for i in range(8):
	# 	print(a[i])
	
	#print(hbyte,lbyte)
	# print(intHB,intLB)
	# print(binary_sum)
	# print(sum_4_digit)
	# print("redun",redun)
	#print("codeword",codeword)
	return(codeword)

if __name__ == "__main__":
	messange = input()
	split_messange = [ord(c) for c in messange]
	#print(split_messange)
	ans = ""
	for data in split_messange:
		#print(data)
		# SUM= 0
		# for digit in str(data):
		# 	SUM += int(digit)
		ans += int_to_binary_8bit(data)
		
		

		#print(Binary,len(Binary))
	print(ans)

