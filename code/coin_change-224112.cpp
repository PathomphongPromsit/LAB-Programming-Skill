/*Python20T
def thon():
    global list_coin,m,n
   
    ans_list = [0 for i in range(n+1)] #fill 0
    ans_list[0] = 1 #base case
 
    for i in range(0,m):
        for j in range(list_coin[i],n+1):
            #print(i,j) #num to coin select
            ans_list[j] += ans_list[j-list_coin[i]]
            #print("alj lci ",ans_list[j],list_coin[i])
    return ans_list[n]
 
if __name__ == "__main__":
    list_coin = [1, 5, 10, 25, 50]
    m = 5
    while(True):
        try:
            n = int(input())
            
            ans = thon()
            print(ans)
        except EOFError:
            break*/
#include <iostream>
#include <string.h>
#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

int thon(int m,int n)
{

	int list_coin[5]={1, 5, 10, 25, 50};
	
    vector<int> ans_list; 			//fill 0
    for (int a =0; a<n+1; a++)
    {
    	ans_list.push_back(0);
	}
    
	ans_list[0] = 1;				//base case
   
    for (int i = 0; i < m; i++)
    {
    	for (int j =list_coin[i]; j<n+1; j++)
    	{
    		ans_list[j] += ans_list[j-list_coin[i]];
		}
	}   
    return ans_list[n];
	
}

int main()
{
	int m =5;
	while(!cin.eof()) 
	{
		int n;
		cin >> n;
		if(cin.eof())
		{
			break;
		}
		//do something
		int ans =0;
		ans = thon(m,n);
		cout << ans << endl;
	}

}
