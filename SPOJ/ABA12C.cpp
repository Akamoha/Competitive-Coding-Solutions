#include<bits/stdc++.h>
#include<limits.h>

#define ll long long int
#define sd(x) scanf("%d", &x);

using namespace std;

int main() {
	int C, c, N, K, p, i, j;
	vector<ll> ans;
	vector<int> prices;
	sd(C);
	ll mn;
	for(c = 0; c < C; c++) {
		sd(N); sd(K);
		ans.clear();
		prices.clear();
		prices.push_back(0);
		ans.push_back(0);
		for(j = 1; j <= K; j++) {
			sd(p);
			prices.push_back(p);
			ans.push_back(p);
		}
		for(j = 2; j <= K; j++) {
			for(i = 1; i < j; i++) {
				if(prices[j-i] != -1 && ans[j] != -1) {
					if(ans[j] == -1)
						ans[j] = ans[i] + prices[j-i];
					else
						ans[j] = min(ans[j], ans[i]+prices[j-i]);
				}
			}
		}
		printf("%lld\n", ans[K]);
	}
}