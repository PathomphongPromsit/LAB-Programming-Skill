/*from __future__ import print_function

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
	
	test_case = int(input())
	for i in range(test_case):
		ingredient = int(input())
		
		ans=0

		x = [int(i) for i in input().split()]
		y = [int(i) for i in input().split()]

		for j in range(ingredient):
			if j == 0:
				ans = int(HCF_GCD(x[j],y[j])/x[j])
				#print("J==0",ans)
			else:
				ans = int(HCF_GCD(ans,HCF_GCD(x[j],y[j])/x[j]))
		print(ans)
		for k in range(ingredient):
			print (int((x[k]*ans)/y[k]),"",end='')
	*/
#include <iostream>
#include <vector>
using namespace std;

int cal_HCF(int x, int y)
{
	//Euclidian algor
	while(y)
	{
		int copy_x;
		copy_x = x;
		x = y;
		y = copy_x % y;
		//x, y = y, x % y;
	}
	return (x);

}

int HCF_GCD(int x, int y)
{
	int HCF;
	int GCD;
	HCF = cal_HCF(x,y);
	GCD = (x*y)/HCF;
	return(GCD);
}
	
int main()
{
	int test_case;
	cin >> test_case;
	for (int i = 0;i < test_case; i++)
	{
		int ingredient;
		cin >> ingredient;
		
		int ans=0;
		int x[ingredient];
		int y[ingredient];
		
		for(int j = 0;j <ingredient;j++)
		{
			cin >> x[j];
		}
		for(int k = 0;k <ingredient;k++)
		{
			cin >> y[k];
		}
		

		for (int l = 0; l < ingredient;l++)
		{
			if (l == 0)
			{
				ans = HCF_GCD(x[l],y[l])/x[l];
			}
			
			else
			{
				ans = HCF_GCD(ans,HCF_GCD(x[l],y[l])/x[l]);
			}
			
			
		}
		
		cout << ans << endl;
		
		for(int m = 0; m < ingredient; m++)
		{
			int gg;
			gg = (x[m]*ans)/y[m];
			cout << gg << " ";
		}
			
	}
		
}
	
	
