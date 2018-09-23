
#include <stdio.h>
#include <limits.h>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
  

int minDistance(int dist[], bool sptSet[],int V)
{
   // Initialize min value
   int min = INT_MAX, min_index;
  
   for (int v = 0; v < V; v++)
     if (sptSet[v] == false && dist[v] <= min)
         min = dist[v], min_index = v;
  
   return min_index;
}

int main()
{
	
	int test;
	cin >> test;
	for (int i = 0; i<test; i++)
	{
		int ball;
		int rope;
		int hold;
		cin >>ball;
		cin>>rope;
		cin>>hold;
		int matrix[ball][ball];
	
		for(int j =0;j<ball;j++)
		{
			for(int k = 0;k<ball;k++)
			{
				matrix[j][k]= 0;
			}
		}
		
		for(int l = 0; l<rope;l++)
		{
			int st_ball;
			int nd_ball;
			int distance;
			cin >> st_ball;
			cin >> nd_ball;
			cin >> distance;
			
			matrix[st_ball][nd_ball]= distance;
			matrix[nd_ball][st_ball]= distance;
			
		}
		
		int V;
		V = ball;
		
		int graph[V][V];
	
		for(int aa =0; aa<V; aa++)
		{
			for(int bb =0;bb<V; bb++)
			{
				graph[aa][bb] = matrix[aa][bb];
			}
		}
		
		int src = hold;
		
		
		// DIJKSTAR find the vertex with minimum distance value
		
		int dist[V];    // The output array.  dist[i] will hold the shortest
                      	// distance from src to i
  
     	bool sptSet[V]; // sptSet[i] will true if vertex i is included in shortest
                     	// path tree or shortest distance from src to i is finalized
  
	    // Initialize all distances as INFINITE and stpSet[] as false
	    for (int m = 0; m < V; m++)
	    {
	    	dist[m] = INT_MAX, sptSet[m] = false;
		}
		
	    // Distance of source vertex from itself is always 0
	    dist[src] = 0;
	  
	    // Find shortest path for all vertices
	    for (int count = 0; count < V-1; count++)
	    {
	    	// Pick the minimum distance vertex from the set of vertices not
	    	// yet processed. u is always equal to src in first iteration.
	    	int u = minDistance(dist, sptSet,V);
	  
	    	// Mark the picked vertex as processed
	    	sptSet[u] = true;
	  
	    	// Update dist value of the adjacent vertices of the picked vertex.
	    	for (int v = 0; v < V; v++)
	  
	    	// Update dist[v] only if is not in sptSet, there is an edge from 
	    	// u to v, and total weight of path from src to  v through u is 
	    	// smaller than current value of dist[v]
	    	if (!sptSet[v] && graph[u][v] && dist[u] != INT_MAX && dist[u]+graph[u][v] < dist[v])
	    	{
	    		dist[v] = dist[u] + graph[u][v];
			}  
	    }
	    
	    int MAX= 0;
	    vector<int> ans;
     	for (int o = 0; o < V; o++)
     	{
     		if(dist[o]<100001)
     		{
     			if(dist[o] > MAX)
     			{
	     			//cout<< MAX;
	     			ans.clear();
	     			MAX = dist[o];
	     			ans.push_back(o);	
				}
				else if(dist[o] == MAX)
				{
					ans.push_back(o);
				}
			}
     		
		}
		//cout << "MAX" << MAX;
		for(int an = 0; an < ans.size(); an++)
		{
			cout << ans[an] << " ";
		}
      	//cout << endl;
	}

}
