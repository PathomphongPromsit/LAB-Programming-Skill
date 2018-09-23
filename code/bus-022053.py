def bus(KK):
	print("GGWP")

if __name__ == "__main__":
	
	while True:
		n,d,r =[int(i) for i in input().split()]
		if n == 0 and d == 0 and r==0:
			break
		else:
			mor=[int(j) for j in input().split()]
			aft=[int(k) for k in input().split()]

			mor.sort()
			aft.sort()

			OT =0
			for i in range(n):
				if mor[i]+aft[0-(i+1)]>d:
					OT+= ((mor[i]+aft[0-(i+1)])-d)*r


			print(OT)
