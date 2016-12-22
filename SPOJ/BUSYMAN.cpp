#include<bits/stdc++.h>

#define sd(x) scanf("%d", &x);
#define sll(x) scanf("%lld", &x);
#define ll long long int

using namespace std;

int main() {
	int T, t, N, n, m, endtime, i, ans;
	vector<pair<int, int> > A;
	sd(T);
	for(t = 0; t < T; t++) {
		sd(N);
		A.clear();
		for(i = 0; i < N; i++) {
			sd(n); sd(m);
			A.push_back(make_pair(m, n));
		}
		sort(A.begin(), A.end());
		endtime = A[0].first;
		ans = 1;
		for(i = 1; i < A.size(); i++) {
			if(endtime <= A[i].second) {
				ans++;
				endtime = A[i].first;
			}
		}
		printf("%d\n", ans);
	}
	return 0;
}