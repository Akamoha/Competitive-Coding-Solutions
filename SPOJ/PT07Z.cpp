#include<stdio.h>
#include<iostream>
#include<map>
#include<vector>

using namespace std;

map<int, vector<int> > adjList;

int reach[10001];

int maxLevel = -1, node = -1;

void dfs(int v, int level) {
	reach[v] = 1;
	for(vector<int>::iterator it = adjList[v].begin(); it != adjList[v].end(); it++) {
		if(reach[*it] != 1) {
			dfs(*it, level+1);
		}
		if(level > maxLevel) {
			maxLevel = level;
			node = v;
		}
	}
}

int main() {
	int N, u, v, i;
	cin>>N;
	for(i = 0; i < N-1; i++) {
		cin>>u>>v;
		adjList[u].push_back(v);
		adjList[v].push_back(u);
	}
	dfs(u, 0);
	u = node;
	node = -1;
	maxLevel = -1;
	for(i = 0; i < 10001; i++) {
		reach[i] = 0;
	}
	dfs(u, 0);
	cout<<maxLevel<<endl;
	return 0;
}