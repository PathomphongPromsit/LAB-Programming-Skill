#include <iostream>
#include <vector>
using namespace std;
int main()
{

	int T;
	cin >> T;
	int Max_x = 0;
	int Max_y = 0;
	std::vector<int> x_attack;;
	std::vector<int> y_attack;;
	std::vector<int> s_attack;;
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
		
		if(s != 0)
		{
			if ((x == 0 ) || (y == 0))
			{
				count+=s;
			}
			else
			{
				x_attack.push_back(x);
				y_attack.push_back(y);
				s_attack.push_back(s);
				LEN++;
			}
		}
	}
	for (int j=0; j<LEN; j++)
	{
		if ((x_attack[j] == Max_x) || (y_attack[j] == Max_y))
			count +=s_attack[j];
	}
	
	cout << count;
	
	
	
}
