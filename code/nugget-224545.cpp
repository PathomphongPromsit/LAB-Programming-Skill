/*Pythom
import math
if __name__ == "__main__":
	n1, p1 = [int(i) for i in input().split()]
	n2, p2 = [int(j) for j in input().split()]
	n3, p3 = [int(k) for k in input().split()]
	N = int(input())
	Min_money = 3000001
	Min_nug = 103001
	GG = int(N/n3)+1
	WP = int(N/n2)+1

	for mk in range(GG):
		for mkk in range(WP):
			#print(mk,mkk)
			c = int(N/n3)-mk
			gg = N-(n3*c)
			b = int(gg/n2)-mkk
			gg = gg-(n2*b)
			a = math.ceil(gg/n1)
			#print (a,b,c)
			if a>=0 and b>=0 and c>=0:
				sum_nug = (a*n1) + (b*n2) + (c*n3)
				sum_money = (a*p1) + (b*p2) + (c*p3)
				if sum_nug == Min_nug:
					if sum_money < Min_money:
						Min_money = sum_money
				elif sum_nug < Min_nug:
					Min_nug = sum_nug
					Min_money = sum_money
	print(Min_money)*/

#include <iostream>
#include <string.h>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;


int main()
{
	int	n1,n2,n3,p1,p2,p3,N;
	cin >>n1;
	cin >>p1;
	cin >>n2;
	cin >>p2;
	cin >>n3;
	cin >>p3;
	cin >>N;
	int Min_money = 3000001;
	int Min_nug = 103001;
	int GG = int(N/n3)+1;
	int WP = int(N/n2)+1;

	for (int mk=0;mk<GG;mk++)
	{
		for (int mkk=0;mkk<WP;mkk++)
		{
			int c = int(N/n3)-mk;
			int gg = N-(n3*c);
			int b = int(gg/n2)-mkk;
			gg = gg-(n2*b);
			float ggg = gg*1.0;
			int a = ceil(ggg/n1);
			//int a = ceil(gg/n1);
			//cout<<a<<" "<<b<<" "<<c<<endl;
			if (a>=0 && b>=0 && c>=0)
			{
				int sum_nug = (a*n1) + (b*n2) + (c*n3);
				int sum_money = (a*p1) + (b*p2) + (c*p3);
				
				if (sum_nug == Min_nug)
				{
					if (sum_money < Min_money)
					{
						Min_money = sum_money;
					}
				}
					
				else if (sum_nug < Min_nug)
				{
					Min_nug = sum_nug;
					Min_money = sum_money;
				}
			}
		}
	}
	cout <<Min_money;
}
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
