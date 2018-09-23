a = []
b = []
n = int(input())
for i in range (n):#insert data into matrix
	data = int(input())
	a.append(data) 
for i in range (n):#insert data into matrix
	data = int(input())
	b.append(data) 
a.sort()
b.sort()


loop1count = 0
loop2count = 0
count = 0


while (loop1count < n) and (loop2count < n):
	# print (loop1count)
	# print (loop2count)

	if a[loop1count] == b[loop2count]:
		count += 1
		loop1count +=1
		loop2count +=1
	elif a[loop1count]<b[loop2count]:
		loop1count += 1
	elif a[loop1count]>b[loop2count]:
		loop2count +=1
	# print (loop1count)
	# print (loop2count)
	# print (count)

# print (a)
# print (b)\

# for i in range (0,n):
# 	print (a[loop1count])
# 	loop1count += 1
#print (a[loop1count])


print (count)
