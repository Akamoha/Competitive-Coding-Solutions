#include<stdio.h>
#include<iostream>
#include<map>
#include<vector>

using namespace std;

int reach[10001];

map<int, vector<int> > adjList;

void dfs(int v) {
	reach[v] = 1;
	for(vector<int>::iterator it = adjList[v].begin(); it != adjList[v].end(); it++) {
		if(reach[*it] != 1) {
			dfs(*it);
		}
	}
}

int main() {
	int N, M, u, v, i;
	cin>>N>>M;
	vector <int> nodes;
	for(i = 0; i < M; i++) {
		cin>>u>>v;
		adjList[u].push_back(v);
		adjList[v].push_back(u);
		nodes.push_back(u);
		nodes.push_back(v);
	}
	if(N != M+1) {
		cout<<"NO"<<endl;
	}
	else {
		dfs(u);
		int flag = 1;
		for(vector<int>::iterator it = nodes.begin(); it != nodes.end(); it++) {
			if(reach[*it] != 1) {
				flag = 0;
				cout<<"NO"<<endl;
				break;
			}
		}
		if(flag) {
			cout<<"YES"<<endl;
		}
	}
	return 0;
}