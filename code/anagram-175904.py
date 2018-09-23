N = int(input())
for i in range(N):
	a = input()
	b = input()
	A = list(a)
	B = list(b)
	A.sort()
	B.sort()

	if A == B:
		print("ANAGRAM")
	else:
		print ("NOT ANAGRAM")

	