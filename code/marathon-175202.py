def cal_HCF(x, y):
#Euclidian algor
	while(y):
		x, y = y, x % y
	return x
def HCF_GCD(x,y):
	
	HCF = cal_HCF(x,y)
	GCD = (x*y)/HCF
	return(GCD)

if __name__ == "__main__":

	N, R = [int(i) for i in input().split()]
	list_time_car = [int(j) for j in input().split()]

	Max_snap = 0
	# Car_max_snap = 0

	first = list_time_car[0]
	for i in range(1,N):
		another = list_time_car[i]
		
		gcd = int(HCF_GCD(first,another))
	

		
		#print(gcd)
		MIN = first
		if first <= another:
			MIN = first
		else:
			MIN = another
		

		Time_limit = MIN*R
		
		snap = Time_limit- (Time_limit % gcd)


		if snap >= Max_snap:
			Max_snap = snap
			# Car_max_snap = i+1
	print(Max_snap)