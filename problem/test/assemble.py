avg = int(input())
set_parang = []
Sum =0
for i in range(avg):
	parang = int(input())
	set_parang.append(parang)
	Sum+=parang
set_parang.sort()
tanos = int(input())
count = 0
if Sum>tanos:
	i=avg-1
	while tanos>=0:
		tanos-=set_parang[i]
		i-=1
		count+=1
	print(count)
else:
	print("YOU DIE")
		