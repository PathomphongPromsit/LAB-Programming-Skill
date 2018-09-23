/*PYTHON
if __name__ == "__main__":
	#code mod from fn to non fn

	nisit = int(input())
	matrix = [-1 for i in range(nisit)]
	
	for i in range(nisit):
		friend = [int(f) for f in input().split()]
		matrix[i]=friend[1:]
	
	test = int(input())

	for k in range(test):
		know_news_list=[]  
		friend_list_new=[]

		first = int(input())
		if nisit ==1:
			print("0")
		else:
			know_news_list.append(-1)
			know_news_list.append(first)
			friend_list_new.append(first)
			num_max = 0
			day_count = 1
			day_max = 0
			new_know = -1
			SUM = 1
			while new_know != 0 and nisit-SUM > num_max and SUM!=nisit:
				list_new = friend_list_new[:]
				friend_list_new=[]
				count_new_man = 0

				for man in list_new:
					friend_list = matrix[man]
					friend_list_new_two=[]
					for people in friend_list:
						if people not in know_news_list:
							know_news_list.append(people)
							friend_list_new_two.append(people)
					
					friend_list_new.extend(friend_list_new_two)
					count_new_man += len(friend_list_new_two)	
					
				new_know = count_new_man
				#print("NK",new_know)
				SUM +=new_know
				if new_know > num_max:
					num_max = new_know
					day_max = day_count

				day_count+=1


			if num_max == 0:
				print(num_max)
			else:
				print(num_max,day_max)		
	*/
	
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
	int nisit;
	cin >> nisit;
	int matrix[nisit][nisit];
	
	for(int i =0;i<nisit;i++)
	{
		for(int j = 0;j<nisit;j++)
		{
			matrix[i][j]= -1;
		}
	}
	
	for (int k =0;k<nisit;k++)
	{
		int Nfriends;
		
		cin >> Nfriends;
		
		for(int l = 0; l < Nfriends; l++)
		{
			int myfriends = 0;
			cin >> myfriends ;
			matrix[k][myfriends] = myfriends;
		}
		
	}
		
	int test;
	cin >> test;
	
	for(int m = 0; m<test; m++)
	{
		vector<int> know_news_list; 
		vector<int> friend_list_new;
		know_news_list.clear();
		friend_list_new.clear();
		
		int first;
		cin >> first;
		if (nisit ==1)
		{
			cout << "0";
		}
		else
		{
		
			know_news_list.push_back(-1);
			know_news_list.push_back(first);
			
			friend_list_new.push_back(first);
			int num_max = 0;
			int day_count = 1;
			int day_max = 0;
			int new_know = -1;
			int SUM = 1;
		
			while (new_know != 0 && nisit-SUM > num_max && SUM!=nisit)
			{
				vector<int> list_new;
				for (int n=0; n<friend_list_new.size(); n++)
				{
					list_new.push_back(friend_list_new[n]);
					
				}	
					
				friend_list_new.clear();
				
				
				int count_new_man = 0;
				
				for (int Pman=0; Pman< list_new.size(); Pman++)
				{
	
					int man; 
					man = list_new[Pman];
					
					vector<int> friend_list;
					
					for (int gg =0; gg<nisit; gg++)
					{
						if (matrix[man][gg] != -1)
						{
							friend_list.push_back(matrix[man][gg]);
						}
					}
		
					vector<int> friend_list_new_two;
					friend_list_new_two.clear();
					
					for(int ggg = 0; ggg<friend_list.size(); ggg++)
					{
						int people;
					 	people = friend_list[ggg];
					 	//cout << people <<endl;
							
						if(find(know_news_list.begin(), know_news_list.end(), people) != know_news_list.end())
						{
							int kkk;
							kkk = 0;
							
						}
						else
						{
							know_news_list.push_back(people);
							friend_list_new_two.push_back(people);
							friend_list_new.push_back(people);
						}
						
							
					}
					//friend_list_new.extend(friend_list_new_two)
					count_new_man += friend_list_new_two.size();	
				}
					
				
				new_know = count_new_man;
				SUM += new_know;
				if (new_know > num_max)
				{
					num_max = new_know;
					day_max = day_count;
				}
				day_count++;
			}
		
			if (num_max == 0)
			{
				cout << num_max << endl;
			}
			else
			{
				cout << num_max << " " <<day_max <<endl;
			}
			
		}
	}
				
}

