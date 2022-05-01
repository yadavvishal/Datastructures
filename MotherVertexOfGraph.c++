class Solution 
{
    public:
    // DFS traversal are use
    // Bool are used for making false
    
    void dfs(vector<int>adj[],int j,bool*visited,int &count)
    {
        visited[j]=true;
        count++;
        for(int i:adj[j])
        {
            if(!visited[i])
                dfs(adj,i,visited,count);
        }
    }
    
    
    //Function to find a Mother Vertex in the Graph.
	int findMotherVertex(int V, vector<int>adj[])
	{
	    for(int i = 0; i<V; i++){
        bool visited[V] = {};
        if(!visited[i]){
            int count = 0;
            dfs(adj, i, visited, count);
            if(V == count) return i;
        }
        }
        return -1;
    }
};
