parat = int(input())
siya = int(input())
set_parang = []
Sum =0
for i in range(siya):
	parang = int(input())
	set_parang.append(parang)
	Sum+=parang

set_parang.sort()
count = 0
if Sum>parat:
	i=siya-1
	while parat>0:
		parat-=set_parang[i]
		i-=1
		count+=1
	print(count)
else:
	print(0)
		

