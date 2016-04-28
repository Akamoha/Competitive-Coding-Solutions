#include<bits/stdc++.h>

#define sd(x) scanf("%d", &x)

using namespace std;

int main() {
	int T, L, E, t, i, j, x;
	long long int mx, temp;
	vector<int> energy, time;
	vector<long long int> ans;
	sd(T);
	for(t = 0; t < T; t++) {
		sd(E); sd(L);
		energy.clear();
		time.clear();
		ans.clear();
		for(i = 0; i <= E; i++) {
			ans.push_back(0);
		}
		for(i = 0; i < L; i++) {
			sd(x);
			energy.push_back(x);
		}
		for(i = 0; i < L; i++) {
			sd(x);
			time.push_back(x);
		}
		for(i = 1; i <= E; i++) {
			mx = ans[i-1];
			for(j = 0; j < L; j++) {
				if(i >= energy[j]) {
					temp = time[j]+ans[i-energy[j]];
					mx = max(mx, temp);
				}
			}
			ans[i] = mx;
		}
		printf("%lld\n", ans[E]);
	}
	return 0;
}