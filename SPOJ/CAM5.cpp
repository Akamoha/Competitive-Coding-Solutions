#include<stdio.h>
#include<iostream>
#include<bits/stdc++.h>

#define slld(x) scanf("%lld", &x)
#define ll long long int

using namespace std;

vector<vector<ll> > g;
vector<ll> visited;

void DFS(ll s) {
	int i;
	visited[s] = 1;
	for(i = 0; i < g[s].size(); i++) {
		if(visited[g[s][i]] == 0) {
			DFS(g[s][i]);
		}
	}
}

int main() {
	ll T, t, N, E, n, e, a, b, count;
	slld(T);
	for(t = 0; t < T; t++) {
		slld(N);
		slld(E);
		g.clear();
		visited.clear();
		count = 0;
		for(n = 0; n < N; n++) {
			vector<ll> emp;
			g.push_back(emp);
			visited.push_back(0);
		}
		for(e = 0; e < E; e++) {
			slld(a); slld(b);
			g[a].push_back(b);
			g[b].push_back(a);
		}
		
		for(n = 0; n < N; n++) {
			if(visited[n] != 0)
				continue;
			count++;
			DFS(n);
		}
		printf("%lld\n", count);
	}
	return 0;
}