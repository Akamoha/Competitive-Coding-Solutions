#include<bits/stdc++.h>

#define sll(x) scanf("%lld", &x)
#define ll long long int
#define mp make_pair

using namespace std;

vector<vector<ll> > g;
vector<ll> covered;
unordered_map<ll, ll> visited;

bool BFS(ll s, ll level) {
	queue<pair<ll, ll> > q;
	q.push(mp(s, level));
	while(!q.empty()) {
		pair<ll, ll> node = q.front(); q.pop();
		if(node.second == -1)
			break;
		if(visited.find(node.first) == visited.end()) {
			visited[node.first] = 1;
			covered[node.first]++;
			if(covered[node.first] > 1) {
				return false;
			}
			ll i;
			for(i = 0; i < g[node.first].size(); i++) {
				if(visited.find(g[node.first][i]) == visited.end()) {
					q.push(mp(g[node.first][i], node.second-1));
				}
			}
		}
	}
	return true;
}

int main () {
	ll T, t, N, R, M, A, B, i, K, S;
	sll(T);
	for(t = 0; t < T; t++) {
		sll(N); sll(R); sll(M);
		g.clear();
		covered.clear();
		for(i = 0; i <= N; i++) {
			vector<ll> emp;
			g.push_back(emp);
			covered.push_back(0);
		}
		for(i = 0; i < R; i++) {
			sll(A); sll(B);
			g[A].push_back(B);
			g[B].push_back(A);
		}
		bool flag = true;
		for(i = 0; i < M; i++) {
			sll(K); sll(S);
			if(covered[K] >= 1) {
				flag = false;
				break;
			}
			visited.clear();
			if(!BFS(K, S)) {
				flag = false;
				break;
			}
		}
		if(flag) {
			bool flag2 = true;
			for(i = 1; i <= N; i++) {
				if(covered[i] != 1) {
					printf("No\n");
					flag2 = false;
					break;
				}
			}
			if(flag2)
				printf("Yes\n");
		} else {
			printf("No\n");
		}
	}
}