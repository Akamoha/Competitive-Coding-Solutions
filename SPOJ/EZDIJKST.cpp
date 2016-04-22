#include<iostream>
#include<stdio.h>
#include<bits/stdc++.h>
#include<unordered_map>

#define mp make_pair
#define slld(x) scanf("%lld", &x);
#define sd(x) scanf("%d", &x);
#define ll long long int

using namespace std;

vector<vector<pair<ll, ll> > > g;
vector<ll> shortestDistance;

void dijkstra(ll s) {
	ll i;
	priority_queue<pair<ll, ll>, vector<pair<ll, ll> >, greater<pair<ll, ll> > > q;
	q.push(mp(0, s));
	unordered_map<ll, ll> seen;
	while(!q.empty()) {
		pair<ll, ll> costv1;
		costv1 = q.top(); q.pop();
		ll cost = costv1.first;
		ll v1 = costv1.second;
		if(seen.find(v1) == seen.end()) {
			seen[v1] = 1;
			shortestDistance[v1] = cost;
			for(i = 0; i < g[v1].size(); i++) {
				ll c = g[v1][i].first;
				ll v2 = g[v1][i].second;
				if(seen.find(v2) == seen.end()) {
					q.push(mp(cost+c, v2));
				}
			}
		}
	}
}
	
int main() {
	ll T, t, V, K, i, a, b, c, A, B;
	slld(T);
	for(t = 0; t < T; t++) {
		slld(V); slld(K);
		g.clear();
		shortestDistance.clear();
		for(i = 0; i <= V; i++) {
			vector<pair<ll, ll> > emp;
			g.push_back(emp);
			shortestDistance.push_back(-1);
		}
		for(i = 0; i < K; i++) {
			slld(a); slld(b); slld(c);
			g[a].push_back(mp(c, b));
		}
		slld(A); slld(B);
		dijkstra(A);
		if(shortestDistance[B] == -1)
			printf("NO\n");
		else
			printf("%lld\n", shortestDistance[B]);
	}
	return 0;
}