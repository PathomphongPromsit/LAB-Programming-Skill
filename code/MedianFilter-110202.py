from __future__ import print_function
wide, hight, s = [int(i) for i in input().split()]
pic = [[int(j) for j in input().split()]for i in range(hight)]
for i in range(hight):
	for j in range(wide):
		median_list = []
		#####################################1
		value = pic[i][j]
		median_list.append(value)
		#####################################2
		if j-1 < 0:
			value = 0
			median_list.append(value)
		else:
			value = pic[i][j-1]
			median_list.append(value)
		####################################3
		try:
			value = pic[i][j+1]
			median_list.append(value)
		except IndexError:
			value = 0
			median_list.append(value)
		####################################4
		if i-1 < 0:
			value = 0
			median_list.append(value)
		else:
			value = pic[i-1][j]
			median_list.append(value)
		###################################5
		try:
			value = pic[i+1][j]
			median_list.append(value)
		except IndexError:
			value = 0
			median_list.append(value)
		
		if s==8:
			####################################6
			if (j-1 < 0) or (i-1 <0):
				value = 0
				median_list.append(value)
			else:
				value = pic[i-1][j-1]
				median_list.append(value)

			#################################7
			if i-1 < 0:
				value = 0
				median_list.append(value)

			else:
				try:
					value = pic[i-1][j+1]
					median_list.append(value)
				except IndexError:
					value = 0
					median_list.append(value)
			#################################8
			if j-1 < 0 :
				value = 0
				median_list.append(value)
			else:
				try:
					value = pic[i+1][j-1]
					median_list.append(value)
				except IndexError:
					value = 0
					median_list.append(value)
			#####################################9
			try:
				value = pic[i+1][j+1]
				median_list.append(value)
			except IndexError:
				value = 0
				median_list.append(value)	
		median_list.sort()
		#print (median_list)
		if s == 4:
			median = median_list[2]
		else:
			median = median_list[4]
		print("%s "%median , end='')
	print()
#647#	
#213#		
#859#
			


