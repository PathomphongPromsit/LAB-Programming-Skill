def fibo(N):
	ans=[]
	ans.append(1)
	ans.append(2)
	ans.append(3)
	for i in range(2,N):
		ans[2] = ans[0]+ans[1]
		ans[0] = ans[1]
		ans[1] = ans[2]
	return(ans[2])
if __name__ == "__main__":
	
	N = int(input())
	if N <4:
		print(N)
	else:
		a = fibo(N)
		print(a)