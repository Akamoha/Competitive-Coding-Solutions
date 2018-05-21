#include<bits/stdc++.h>

using namespace std;

vector<vector<int> > g;
unordered_map<int, int> size;

int findSize(int s, int parent) {
	
	int curSize = 1;
	for(int i = 0; i < g[s].size(); i++) {
		if(g[s][i] != parent) {
			curSize += findSize(g[s][i], s);
		}
	}
	size[s] = curSize;
	
	return curSize;
}

int solve(int s, int parent) {
	
	int ans = 0;
	for(int i = 0; i < g[s].size(); i++) {
		if(g[s][i] != parent) {
			if(size[g[s][i]] % 2 == 0) {
				ans += 1+solve(g[s][i], s);
			} else {
				ans += solve(g[s][i], s);
			}
		}
	}
	
	return ans;
}

int main() {
	
	int n, i, u, v;
	
	cin>>n;
	
	for(i = 0; i <= n; i++) {
		vector<int> emp;
		g.push_back(emp);
	}
	
	for(i = 0; i < n-1; i++) {
		cin>>u>>v;
		g[u].push_back(v);
		g[v].push_back(u);
	}
	
	if(n % 2 != 0) {
		cout<<-1<<endl;
	} else {
		findSize(1, 0);
		cout<<solve(1, 0);
	}
	
	return 0;
}