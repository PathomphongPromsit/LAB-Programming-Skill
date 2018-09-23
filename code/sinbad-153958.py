#647#	
#213#		
#859#
def land(i,j,num_chk):

		#####################################2
		if j-1 < 0:
			value = 0
		else:
			value = Map[i][j-1]
			if value == num_chk :#or value == 1:
				Map[i][j] = num_chk
				Map[i][j-1]= num_chk
		####################################3
		try:
			value = Map[i][j+1]
			if value == num_chk :#or value == 1:
				Map[i][j] = num_chk
				Map[i][j+1]= num_chk

		except IndexError:
			value = 0
		####################################4
		if i-1 < 0:
			value = 0
		else:
			value = Map[i-1][j]
			if value == num_chk :# or value == 1:
				Map[i][j] = num_chk
				Map[i-1][j]= num_chk

		###################################5
		try:
			value = Map[i+1][j]
			if value == num_chk :#or value == 1:
				Map[i][j] = num_chk
				Map[i+1][j]= num_chk

		except IndexError:
			value = 0
		
		
		####################################6
		if (j-1 < 0) or (i-1 <0):
			value = 0
		else:
			value = Map[i-1][j-1]
			if value == num_chk :#or value == 1:
				Map[i][j] = num_chk
				Map[i-1][j-1]= num_chk


		#################################7
		if i-1 < 0:
			value = 0
		else:
			try:
				value = Map[i-1][j+1]
				if value == num_chk :#or value == 1:
					Map[i][j] = num_chk
					Map[i-1][j+1]= num_chk
			except IndexError:
				value = 0
		#################################8
		if j-1 < 0 :
			value = 0
		else:
			try:
				value = Map[i+1][j-1]
				if value == num_chk :#or value == 1:
					Map[i][j] = num_chk
					Map[i+1][j-1]= num_chk

			except IndexError:
				value = 0
		#####################################9
		try:
			value = Map[i+1][j+1]
			if value == num_chk :#or value == 1:
				Map[i][j] = num_chk
				Map[i+1][j+1]= num_chk

		except IndexError:
			value = 0
	###########################################
		if (Map[i][j]== num_chk):
			if (j-1 < 0) or (i-1 <0):      ################4 LEFT ON
				value = 0
			else:
				value = Map[i-1][j-1]
				if value == 1 :#or value == 1:
					Map[i-1][j-1]= num_chk
			
			if i-1 < 0:                     ###############6 ON
				value = 0
			else:
				value = Map[i-1][j]
				if value == 1 :# or value == 1:
					Map[i-1][j]= num_chk
				
			if i-1 < 0:                  ################7 RIGHT ON
				value = 0
			else:
				try:
					value = Map[i-1][j+1]
					if value == 1 :#or value == 1:
						Map[i-1][j+1]= num_chk
				except IndexError:
					value = 0


if __name__ == "__main__":
	m, n = [int(i) for i in input().split()]
	Map = [[int(j) for j in input().split()]for k in range(n)]
	

	##################################################################
	num_chk = 0      #set first find to num_chk
	stop_loop = True
	while stop_loop:
		chk = True
		for i in range(n):
			if chk == False:
				break
			for j in range(m):
				if (Map[i][j] == 1):
					num_chk -= 1
					Map[i][j] = num_chk
					chk = False
					break
		
		if chk == False:    #chek up land mix
			for i in range(n):
				for j in range(m):
					if (Map[i][j] == 1):
						count = land(i,j,num_chk)
						count_land = count
			for i in range(n):
				for j in range(m):
					if (Map[i][j] == 1):
						count = land(i,j,num_chk)
						count_land = count
			for i in range(n):
				for j in range(m):
					if (Map[i][j] == 1):
						count = land(i,j,num_chk)
						count_land = count


		elif chk == True:
			stop_loop = False
			print (abs(num_chk))



	######################################################################	
	

	#print (num_chk)

	#for i in range(n):
	#	print (Map[i])
