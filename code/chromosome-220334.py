n = input()
N = list(n)

if N[0] == 0 or N[0]== 'A' or N[0]== 'B' or N[0]=='C' or N[0]== 'D' or N[0]== 'E' or N[0]== 'F':
	if N[-1] == 0 or N[-1]== 'A' or N[-1]== 'B' or N[-1]=='C' or N[-1]== 'D' or N[-1]== 'E' or N[-1]== 'F':
		# del N[0]
		# del N[-1]
		
		findAF = False
		findFC = False
		chk = True
		chkA = False
		chkF = False
		chkC = True

		for i in range(len(N)):
			if i != len(N)-1:
				next_index = i+1
				##MID###
				if N[i] == 'A' and N[next_index] == 'F':
					findAF = True
				elif N[i] == 'F' and N[next_index] == 'C':
					findFC = True

				if N[i] == 'A' and N[next_index] == 'A':
					chk = True
				elif N[i] == 'A' and N[next_index] == 'F':
					chk = True
				elif N[i] == 'F' and N[next_index] == 'F':
					chk = True
				elif N[i] == 'F' and N[next_index] == 'C':
					chk = True
				elif N[i] == 'C' and N[next_index] == 'C':
					chk = True
				##HEAD
				elif (N[i]== 'A' or N[i]== 'B' or N[i]=='C' or N[i]== 'D' or N[i]== 'E' or N[i]== 'F') and (N[next_index] == 'A'):
					chk = True
				###TAIL
				elif (N[i] == 'C') and (N[next_index]== 'A' or N[next_index]== 'B' or N[next_index]=='C' or N[next_index]== 'D' or N[next_index]== 'E' or N[next_index]== 'F'):
					chk = True
				
				else:
					chk = False
					break
			if N[i] == 'A':
				chkA = True
			if N[i] == 'F':
				chkF = True
			if N[i] == 'C':
				chkC = True
				
		if findAF and findFC and chk and chkA and chkF and chkC:
			print ("Infected!")
		else:
			print ("Good")

			

	else:
		print ("Good")
else:
	print ("Good")

