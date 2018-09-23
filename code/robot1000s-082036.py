control = input()
miss = int(input())
sumN = 0
sumE = 0
sumS =0
sumW = 0

for i in control:
	if i == "N":
		sumN +=1
	elif i == "E":
		sumE +=1
	elif i == "S":
		sumS +=1
	elif i == "W":
		sumW +=1
minX= min(sumE, sumW)
minY= min(sumN, sumS)
x = sumE-sumW
y = sumN-sumS
if (minX+minY) < miss:
	oil = (abs(x)+abs(y)+(minX+minY)-(miss-(minX+minY)))*2
	#oil = (abs(x)+abs(y)+(minX+minY))*2
else:
	oil = (abs(x)+abs(y)+miss)*2
print (oil)
