/*PYTHON 70
if __name__ == "__main__":
	N = int(input())
	
	st_list=[]
	nd_list=[]

	for i in range(N):
		a,b = [int(j) for j in input().split()]
		st_list.append(a)
		nd_list.append(b)
	st_list.sort()
	nd_list.sort()
	
	Max_attack =0
	index_Max_attack =0

	for j in range(N):
		attack = 1
		for k in range(j+1,N):
			if st_list[k]<=nd_list[j]:
				attack+=1
			elif st_list[k]>nd_list[j]:
				if attack>Max_attack:
					Max_attack=attack
					index_Max_attack = nd_list[j]
			
	print(index_Max_attack)*/
#include <iostream>
#include <string.h>
#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;
int main(){
		
	int N=0;
	cin >> N;	
	
	vector <int> st_list; 
	vector<int> nd_list; 
	
	int st=0,nd=0;
	
	for(int i=0;i<N;i++)
	{
		cin >> st;
		cin >> nd;
		
		st_list.push_back(st);
		nd_list.push_back(nd);
	}
	
	sort(st_list.begin(),st_list.end());
	sort(nd_list.begin(),nd_list.end());
	
	int Max_attack = 0;
	int index_Max_attack =0;
	int attack;
	for(int j=0;j<N;j++)
	{
		attack =1;
		
		for(int k=j+1;k<N;k++)
		{		
			if(st_list[k] <= nd_list[j])
			{ 
				attack+=1;
			}
			else if(st_list[k] > nd_list[j])
			{ 
				if(attack > Max_attack)
				{
					Max_attack = attack;
					index_Max_attack = nd_list[j];
						
				}
				break;
			}
		}
	}
	
	cout << index_Max_attack;
}
