#include<stdio.h>
#include<iostream>
#include<bits/stdc++.h>

#define slld(x) scanf("%lld", &x);
#define ll long long int

using namespace std;

vector<vector<ll> > g;
vector<ll> depths;

void DFS(ll s, ll depth) {
	depths[s] = depth;
	int i;
	for(i = 0; i < g[s].size(); i++)
		if(depths[g[s][i]] == -1)
			DFS(g[s][i], depth+1);
}

int main() {
	ll T, N, t, n, a, b, maxdepthnode;
	slld(T);
	for(t = 0; t < T; t++) {
		slld(N);
		g.clear();
		depths.clear();
		for(n = 0; n < N; n++) {
			vector<ll> emp;
			g.push_back(emp);
			depths.push_back(-1);
		}
		for(n = 0; n < N-1; n++) {
			slld(a); slld(b);
			g[a].push_back(b);
			g[b].push_back(a);
		}
		DFS(0, 0);
		maxdepthnode = 0;
		for(n = 0; n < N; n++) {
			if(depths[n] > depths[maxdepthnode]) {
				maxdepthnode = n;
			}
		}
		depths.clear();
		for(n = 0; n < N; n++) {
			depths.push_back(-1);
		}
		DFS(maxdepthnode, 0);
		maxdepthnode = 0;
		for(n = 0; n < N; n++) {
			if(depths[n] > depths[maxdepthnode]) {
				maxdepthnode = n;
			}
		}
		if(depths[maxdepthnode] % 2 == 0)
			printf("%lld\n", depths[maxdepthnode]/2);
		else
			printf("%lld\n", (depths[maxdepthnode]+1)/2);
	}
}