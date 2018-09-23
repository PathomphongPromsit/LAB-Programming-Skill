/* PYTHON
def friend_sug(k,n,matrix):
	friend =[]
	not_friend =[]
	k-=1
	for i in range(n):
		if i != k:
			if matrix[k][i] == 0:
				not_friend.append(i)
			else:
				friend.append(i)

	ans = []
		
	for j in not_friend:
		#print("notF",j)
		count = 0
		for i in friend:
			if (matrix[j][i] ==1):
				count += 1
			
		if count != 0:
			ans.append((count,j))

	#ans_two  = sorted(ans,key=lambda x:(-x[0],x[-1]))
	#print("ans",ans)
	ans_two = sorted(ans,key=lambda x:-x[0])
	#print("ans2",ans)
	
	LA = len(ans_two)
	if LA <= 10:
		for i in range(LA):
			# if ans_two[0][i] >0:
			print(ans_two[i][1]+1,ans_two[i][0])
			# else:
			# 	break
	else:
		for i in range(10):
			# if ans_two[0][i] >0:
			print(ans_two[i][1]+1,ans_two[i][0])
			# else:
			# 	break

if __name__ == "__main__":
	n,m = [int(i) for i in input().split()]

	matrix = [[0 for i in range(n)]for j in range(n)]

	for k in range(m):
		x,y = [int(i) for i in input().split()]
		
		x-=1
		y-=1
		matrix[x][y] = 1
		matrix[y][x] = 1
	# for i in range(n):
	# 	print(matrix[i])
	k = int(input())
        
	friend_sug(k,n,matrix)*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


bool sortbyCount(const pair<int,int> &a,const pair<int,int> &b)
{
	if(a.first == b.first)
	{
		return(a.second < b.second);
	}
	else
	{
		return (a.first > b.first );
	}
}


int main()
{
	int n;
	int m;
	cin >> n;
	cin >> m;
	int matrix[n][n];

	
	for(int i=0; i<m;i++)
	{
		int x;
		int y;
		cin >> x;
		cin >> y;
		x--;
		y--;
		matrix[x][y]= 1;
		matrix[y][x]= 1;
	}
	int k;
	cin >> k;
	
	
	vector<int> friends;
	vector<int> not_friend;
	
	k-=1;
	int size_friend =0;
	int size_Nfriend = 0;
	
	for(int j = 0;j<n;j++)
	{
		if (j != k)
		{
			if (matrix[k][j] == 1)
			{
				friends.push_back(j);
				size_friend++;
			}
			else
			{
				not_friend.push_back(j);
				size_Nfriend++;
			}	
		}
	}
	
	vector < pair<int, int> > ans;
	
	int size_ans=0;
	for(int g = 0; g<size_Nfriend;g++)
	{
		
		int b = not_friend[g];
		int count = 0;
		for(int h = 0; h<size_friend;h++)
		{
			int c = friends[h];
			if (matrix[b][c] ==1)
			{
				count++;
			}		
		}
		
		if (count != 0)
		{
			//ans.push_back(pair<int,int> (b,count) );
			ans.push_back(pair<int,int> (count,b) );
			size_ans++;
		}	
	}
	
	
	
	//sort(ans.begin(), ans.end(), sortbysec);
	//sort( ans.begin(), ans.end());
	
	sort(ans.begin(), ans.end(), sortbyCount);
	//sort(ans.begin(), ans.end(), sortbyNo);
	if (size_ans <= 10)
	{
		for(int g = 0 ; g < size_ans; g++)
		{
			//cout << ans[g].first+1 <<" "<< ans[g].second<<endl;
			cout << ans[g].second+1 <<" "<< ans[g].first <<endl;
		}
			
	}
		
	else
	{
		for (int gg = 0; gg<10;gg++)
		{
			//cout << ans[gg].first+1 <<" "<< ans[gg].second<<endl;
			cout << ans[gg].second+1 <<" "<< ans[gg].first <<endl;
		}
			
	}	
}

