#include<bits/stdc++.h>

#define sll(x) scanf("%lld", &x);
#define ll long long int
#define mp make_pair

using namespace std;

vector<vector<pair<ll, ll> > > g;
vector<ll> depths;

void DFS(ll s, ll p, ll depth) {
	ll i;
	depths[s] = depth;
	for(i = 0; i < g[s].size(); i++) {
		if(g[s][i].second != p) {
			DFS(g[s][i].second, s, depth+g[s][i].first);
		}
	}
}

int main() {
	ll T, t, N, a, b, c, i;
	sll(T);
	for(t = 0; t < T; t++) {
		sll(N);
		g.clear();
		depths.clear();
		for(i = 0; i <= N; i++) {
			vector<pair<ll, ll> > emp;
			g.push_back(emp);
			depths.push_back(-1);
		}
		for(i = 0; i < N-1; i++) {
			sll(a); sll(b); sll(c);
			g[a].push_back(mp(c, b));
			g[b].push_back(mp(c, a));
		}
		DFS(1, 0, 0);
		ll maxdepthnode = 1;
		for(i = 2; i <= N; i++) {
			if(depths[maxdepthnode] < depths[i])
				maxdepthnode = i;
		}
		for(i = 0; i <= N; i++) {
			depths.push_back(-1);
		}
		DFS(maxdepthnode, 0, 0);
		maxdepthnode = 1;
		for(i = 2; i <= N; i++) {
			if(depths[maxdepthnode] < depths[i])
				maxdepthnode = i;
		}
		printf("%lld\n", depths[maxdepthnode]);
	}
	return 0;
}