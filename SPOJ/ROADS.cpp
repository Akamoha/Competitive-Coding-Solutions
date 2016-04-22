#include<iostream>
#include<stdio.h>
#include<bits/stdc++.h>
#include<unordered_map>

#define mp make_pair
#define slld(x) scanf("%lld", &x);
#define sd(x) scanf("%d", &x);
#define ll long long int

using namespace std;

typedef pair<pair<ll, ll>, ll> tuple;

vector<vector<pair<pair<ll, ll>, ll> > > g;
vector<ll> shortestDistance;

ll N, K;

ll dijkstra(ll s) {
	ll i;
	priority_queue<pair<pair<ll, ll>, ll>, vector<pair<pair<ll, ll>, ll> >, greater<pair<pair<ll, ll>, ll> > > q;
	q.push(mp(mp(0, 0), s));
	while(!q.empty()) {
		pair<pair<ll, ll>, ll> costtollv1;
		costtollv1 = q.top(); q.pop();
		ll cost = costtollv1.first.first;
		ll toll = costtollv1.first.second;
		ll v1 = costtollv1.second;
		shortestDistance[v1] = cost;
		if(v1 == N) {
			return toll;
		}
		for(i = 0; i < g[v1].size(); i++) {
			ll c = g[v1][i].first.first;
			ll t = g[v1][i].first.second;
			ll v2 = g[v1][i].second;
			if(toll+t <= K) {
				q.push(mp(mp(cost+c, toll+t), v2));
			}
		}
	}
	return -1;
}

int main() {
	ll tc, t, R, S, D, L, T, i;
	slld(tc);
	for(t = 0; t < tc; t++) {
		slld(K);
		slld(N);
		slld(R);
		g.clear();
		shortestDistance.clear();
		for(i = 0; i <= N; i++) {
			vector<pair<pair<ll, ll>, ll> > emp;
			g.push_back(emp);
			shortestDistance.push_back(-1);
		}
		for(i = 0; i < R; i++) {
			slld(S); slld(D); slld(L); slld(T);
			g[S].push_back(mp(mp(L, T), D));
		}
		ll res = dijkstra(1);
		if(res != -1)
			printf("%lld\n", shortestDistance[N]);
		else
			printf("-1\n");
	}
	return 0;
}