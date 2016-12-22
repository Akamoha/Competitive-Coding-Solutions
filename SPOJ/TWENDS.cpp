#include<bits/stdc++.h>

#define ll long long int
#define sll(x) scanf("%lld", &x);

using namespace std;

vector<ll> A;
ll n;

ll memo[2000][2000];

ll max(ll a, ll b) {
	return a>b?a:b;
}

ll score(ll l, ll r) {
	if(l > r) {
		return 0;
	}
	if(memo[l][r] != -1) {
		return memo[l][r];
	}
	return(memo[l][r] = max(
		A[l+1]>=A[r]?score(l+2,r)+A[l]:score(l+1,r-1)+A[l],
		A[l]>=A[r-1]?score(l+1,r-1)+A[r]:score(l,r-2)+A[r]
	));
}

ll sum() {
	ll i, res = 0;
	for(i = 0; i < n; i++) {
		res += A[i];
	}
	return res;
}

int main() {
	ll c = 1, i, j, x, ans;
	while(1) {
		A.clear();
		sll(n);
		if(n == 0)
			break;
		for(i = 0; i < n+5; i++) {
			for(j = 0; j < n+5; j++) {
				memo[i][j] = -1;
			}
		}
		for(i = 0; i < n; i++) {
			sll(x);
			A.push_back(x);
		}
		ans = 2*score(0,n-1)-sum();
		printf("In game %lld, the greedy strategy might lose by as many as %lld points.\n", c++, ans);
	}
}