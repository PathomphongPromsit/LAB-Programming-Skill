def int_to_binary_8bit(data):
	#binary = format(data, 'b')
	#digit_8 = str(binary).zfill(8)
	
	hbyte = data[0:4]
	lbyte = data[4:8]
	redun = data[8:12]
	#print(hbyte,lbyte,redun)

	intHB = int(hbyte, 2)
	intLB = int(lbyte, 2)
	intRD = int(redun, 2)
	#print(intHB,intLB,intRD)
	
	SUM = intHB+intLB+intRD
	binary_sum = format(SUM, 'b')
	
	sum_4_digit = binary_sum
	if SUM > 15:
		sum_4_digit = binary_sum[1]+binary_sum[2]+binary_sum[3]+binary_sum[4]

	sum_4_digit = str(sum_4_digit).zfill(4)
	#print(sum_4_digit)


	toggle = ""
	for i in range(4):		
		if sum_4_digit[i] == "0":
			toggle += "1"
		else:
			toggle += "0"
	#print(toggle)
	
	if toggle != "0000":
		#print ("#")
		return "#"
	else:
		binary_word = data[0:8]
		#print(chr(int(binary_word[:], 2)))
		return(chr(int(binary_word[:], 2)))

	#codeword = digit_8+redun
	
	# for i in range(8):
	# 	print(a[i])
	
	#print(hbyte,lbyte)
	# print(intHB,intLB)
	# print(binary_sum)
	# print(sum_4_digit)
	# print("redun",redun)
	#print("codeword",codeword)
	#return(codeword)

if __name__ == "__main__":
	messange = input()
	#split_messange = [ord(c) for c in messange]
	LM = len(messange)
	No_of_chr = int(LM/12)
	
	ans = ""
	for i in range(No_of_chr):
		start = i*12
		stop = start+11
		split_messange = messange[start:stop+1]
		#print(start,stop)
		#print(split_messange)
		ans += int_to_binary_8bit(split_messange)
		#int_to_binary_8bit(split_messange)
	print(ans)

