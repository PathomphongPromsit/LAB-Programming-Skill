def paint(hight,count):   #paint Row
	############CHK EMPTY ##################
	try:
		Min = min(hight)

	except ValueError:
		Min = 0
	if Min == 0:  
		return count
	elif Min != 0:
		l = len(hight)
	########################################
				#paint Column
	
	if Min > l:  
	    count = l
	    return count


	######################################
				#paint Low
	else:
		count = Min
		
	
		for i in range(l):  # DELETE PAINTED
			
			hight[i] = hight[i]-Min
		
		#NEW BLOCK RECURSIVE#
		len_new = len(hight)
		#Sent sub list to paint
		while len_new != 0:
			sublist=[]
			for i in range(len_new):
				

				if (hight[i] != 0): #value != 0 add sublist
					if (len_new ==1):  # size 1 have value
						sublist.append(hight[i])
						len_new = 0
					
					elif (i == len_new-1):  # last index
						sublist.append(hight[i])
						del hight[0:len_new]
						len_new = len(hight)
					else:
						sublist.append(hight[i])
				elif hight[i] == 0:	# value = 0 cut list
					del hight[0:i+1]
					len_new = len(hight)
					break
			try:
				m = min(sublist)

			except ValueError:
				m = 0
			if m != 0:
				#print(sublist)
				count = count+paint(sublist,count)
		if count > l:
			return l
		else:
			return count

######################### MAIN ##################
if __name__ == "__main__":
	plate = int(input())
	hight = [int(i) for i in input().split()]
	
	count = 0
	count = count + paint(hight,count)
	print (count)
	