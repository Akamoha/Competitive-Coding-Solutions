#include<bits/stdc++.h>

#define pb push_back
#define mp make_pair
#define INF 1000000007

using namespace std;

int n, m, k, s, j, a, u, v, town, cost;
vector<int> goods;
vector<int> g[100002];
vector<vector<int> > visited;
vector<int> empty;

void BFS(int good) {
	queue<pair<int, int> > q;
	for(int i = 1; i < n+1; i++) {
		if(goods[i] == good)  {
			q.push(mp(i, 0));
			visited[i][good] = 0;
		}
	}
	while(!q.empty()) {
		pair<int, int> townAndCost = q.front();
		q.pop();
		town = townAndCost.first;
		cost = townAndCost.second;
		for(int neighbour : g[town]) {
			if(visited[neighbour][good] > cost+1) {
				visited[neighbour][good] = cost+1;
				q.push(mp(neighbour, cost+1));
			}
		}
	}
	return;
}

int main() {
	
	cin>>n>>m>>k>>s;
	
	goods.pb(0);
	for(int i = 0; i < n; i++) {
		cin>>a;
		goods.pb(a);
	}
	
	for(int i = 0; i < m; i++) {
		cin>>u>>v;
		g[u].pb(v);
		g[v].pb(u);
	}
	
	for(int i = 0; i < k+1; i++) {
		empty.pb(INF);
	}
	for(int i = 0; i < n+1; i++) {
		visited.pb(empty);
	}
	
	for(int i = 1; i < k+1; i++) {
		BFS(i);
	}
	
	for(int i = 1; i < n+1; i++) {
		nth_element(visited[i].begin(), visited[i].begin()+s, visited[i].begin()+k+1);
		int ans = 0;
		for(int j = 0; j < s; j++) {
			ans += visited[i][j];
		}
		cout<<ans<<" ";
	}
	cout<<endl;
	return 0;
}