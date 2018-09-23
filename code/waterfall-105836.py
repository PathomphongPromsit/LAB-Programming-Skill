def cal_m(x1, y1, x2, y2):
	m =(y2-y1)/(x2-x1)
	
	return m


def save_line(x1, y1, x2, y2):
	m = cal_m(x1, y1, x2, y2)
	b = y1-( m * x1)
	line_list.append((x1, y1, x2, y2, m, b))

def check_in_line(X):
	global line_list
	for i in range(len(line_list)):
		x1 = line_list[i][0]
		y1 = line_list[i][1]
		x2 = line_list[i][2]
		y2 = line_list[i][3]

		if (x1<= X <= x2) or (x2<= X <=x1): #on line
			if (x1 < X < x2) or (x2< X <x1):# in mid line 
				in_list.append(i) 
			elif X==x1 or X==x2:  # in edge line
				if y1<y2 and X == x2:
					in_list.append(i)
				elif y2<y1 and X == x1:
					in_list.append(i)
					



def cal_near(X,Y):
	global in_list
	global line_list
	
	near_min = 200001
	near_line =-1
	for data in in_list:
		m = line_list[data][4]
		b = line_list[data][5]
		y_on_line = m*X+b
		#print ("yOnLine",y_on_line)

		
		if y_on_line<=Y:
			distance = abs(Y-y_on_line)
			#print("near dis",distance)
			if distance < near_min:
				near_min = distance
				near_line = data
	return near_line

def water(X,Y):
	global in_list
	global line_list
	in_list=[] #Number line point scope
	check_in_line(X)
	#print(in_list)
	near_line = cal_near(X,Y)
	if near_line == -1:
		print(X)
	else:
		x1 = line_list[near_line][0]
		y1 = line_list[near_line][1]
		x2 = line_list[near_line][2]
		y2 = line_list[near_line][3]

		if y1<y2:
			water(x1,y1)
		else:
			water(x2,y2)




	


	

if __name__ == "__main__":
	line_list=[] #data of line xyxymb
	line = int(input())
	for i in range(line):
		x1, y1, x2, y2 = [int(j) for j in input().split()]
		save_line(x1, y1, x2, y2)
	#print("lineList",line_list)
	test = int(input())
	for k in range(test):
		X, Y = [int(l) for l in input().split()]
		in_list=[]
		water(X,Y)

		

