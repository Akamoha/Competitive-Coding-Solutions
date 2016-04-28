#include<bits/stdc++.h>

#define sd(x) scanf("%d", &x);
#define sll(x) scanf("%lld", &x);
#define ll long long int
#define INF 999999999

using namespace std;

int main() {
	int T, t, E, F, P, W, N, i, j, tw;
	vector<int> weight, value;
	vector<ll> ans;
	ll mn;
	sd(T);
	for(t = 0; t < T; t++) {
		sd(E); sd(F);
		tw = F-E;
		sd(N);
		weight.clear();
		value.clear();
		ans.clear();
		for(i = 0; i < N; i++) {
			sd(P); sd(W);
			weight.push_back(W);
			value.push_back(P);
		}
		for(i = 0; i <= tw; i++) {
			ans.push_back(0);
		}
		for(i = 1; i <= tw; i++) {
			mn = INF;
			for(j = 0; j < N; j++) {
				if(i >= weight[j]) {
					mn = min(mn, ans[i-weight[j]]+value[j]);
				}
			}
			ans[i] = mn;
		}
		if(ans[tw] == INF)
			printf("This is impossible.\n");
		else
			printf("The minimum amount of money in the piggy-bank is %lld.\n", ans[tw]);
	}
	return 0;
}