#include <iostream>
#include <vector>
using namespace std;
int main()
{
	/* PYTHON 90T WTF!
	T = int(input())
	Max_x = 0
	Max_y = 0
	x_attack=[]
	y_attack =[]
	LEN = 0
	count = 0
	for i in range(T):
		x,y,s = [int(i) for i in input().split()]
		if x > Max_x:
			Max_x=x
		if y > Max_y:
			Max_y = y
		
		if s == 0:
			if x == 0 or y == 0:
				count+=1
			else:
				x_attack.append(x)
				y_attack.append(y)
				LEN +=1
	
	print("MXMYL",Max_x,Max_y,LEN)
	for i in range(LEN):
		if x_attack[i] == Max_x or y_attack[i] == Max_y:
			count +=1
	print(count)*/
	
	//CPP
	int T;
	cin >> T;
	int Max_x = 0;
	int Max_y = 0;
	std::vector<int> x_attack;;
	std::vector<int> y_attack;;
	int LEN = 0;
	int count = 0;
	for (int i=0; i<T; i++)
	{
		int x;
		int y;
		int s;
		cin >> x;
		cin >> y;
		cin >> s;
		if(x > Max_x)
		{
			Max_x = x;
		}
		if(y > Max_y)
		{
			Max_y = y;
		}
		
		if(s == 0)
		{
			if ((x == 0 ) || (y == 0))
			{
				count++;
			}
			else
			{
				x_attack.push_back(x);
				y_attack.push_back(y);
				LEN++;
			}
		}
	}
	for (int j=0; j<LEN; j++)
	{
		if ((x_attack[j] == Max_x) || (y_attack[j] == Max_y))
			count +=1;
	}
	
	cout << count;
	
	
	
}
