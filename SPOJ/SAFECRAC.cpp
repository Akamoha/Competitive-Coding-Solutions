#include<bits/stdc++.h>

#define sll(x) scanf("%lld", &x);
#define ll long long int
#define MOD 1000000007
#define pb push_back

using namespace std;

ll DP[100002][10];
ll N;

vector<vector<ll> > adj;

void precompute() {
	int i, j, k;
	for(j = 0; j < 10; j++) {
		vector<ll> emp;
		adj.pb(emp);
		DP[1][j] = 1;
	}
	adj[0].pb(7);
	adj[1].pb(2);
	adj[1].pb(4);
	adj[2].pb(1);
	adj[2].pb(3);
	adj[2].pb(5);
	adj[3].pb(2);
	adj[3].pb(6);
	adj[4].pb(1);
	adj[4].pb(5);
	adj[4].pb(7);
	adj[5].pb(2);
	adj[5].pb(4);
	adj[5].pb(6);
	adj[5].pb(8);
	adj[6].pb(3);
	adj[6].pb(5);
	adj[6].pb(9);
	adj[7].pb(0);
	adj[7].pb(4);
	adj[7].pb(8);
	adj[8].pb(5);
	adj[8].pb(7);
	adj[8].pb(9);
	adj[9].pb(6);
	adj[9].pb(8);
	for(i = 2; i <= 100001; i++ ) {
		for(j = 0; j < 10; j++) {
			DP[i][j] = 0;
			for(k = 0; k < adj[j].size(); k++) {
				DP[i][j] = (DP[i][j] + DP[i-1][adj[j][k]])%MOD;
			}
		}
	}
}

int main() {
	ll T, t, i, ans;
	sll(T);
	precompute();
	for(t = 0; t < T; t++) {
		sll(N);
		ans = 0;
		for(i = 0; i < 10; i++)
			ans = (ans + DP[N][i])%MOD;
		printf("%lld\n", ans);
	}
	return 0;
}