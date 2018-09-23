from __future__ import print_function
def chk_tail(A,B):
	LB = len(B)
	for i in range(1,LB+1):  #ABC  1 2 3  -3 -2 -1
		if B[-i] == A[-1]:   #B[-i] = tail to head   A[-1]= tail
			C = B[:] #copy list
			E = B[:]
			if i == 1:
				D = C
				del E[:]
			else:
				del C[(-i)+1:]  #del i to tail
				D = C
				del E[:-i+1]

			chk = chk_equa(A,D,E)	
			if chk:
	 			return chk
	mix_list = A+B
	return mix_list
def chk_equa(A,D,E):
	
	LD = len(D)
	
	if D == A[-LD:]:
		mix_list = A+E
		return mix_list
		
	else:
	 	return False
if __name__ == "__main__":
	N = int(input())
	for i in range(N):
		a = input()
		b = input()
		A = list(a)
		B = list(b)
		LA = len(A)
		LB = len(B)	
		if LA > LB and b in a:
			for i in A:
				print(i, end='')
			print()
		elif LB > LA and a in b:
			for i in B:
				print(i, end='')
			print()
		elif LA == LB and a in b:
			for i in A:
	 			print(i, end='')
			print()

		else:
			chkAB = chk_tail(A,B)
			chkBA = chk_tail(B,A)
			if len(chkAB) < len(chkBA):
				for i in chkAB:
			 		print(i, end='')
				print()
			elif len(chkAB) == len(chkBA) :
				if chkAB<chkBA:
					for i in chkAB:
			 			print(i, end='')
					print()
				else:
					for i in chkBA:
						print(i, end='')
				print()

			else:
				for i in chkBA:
			 		print(i, end='')
				print()