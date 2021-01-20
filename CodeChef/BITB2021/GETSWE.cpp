#include<bits/stdc++.h>
#define ll long long int

using namespace std;

void solve() {
	int N;
	cin>>N;
	vector<ll> A, A_CSA, B_CSA;
	ll a, a_cur=0, b_cur=0;
	A_CSA.push_back(0);
	B_CSA.push_back(0);
	for(int i = 0; i < N; i++) {
		cin>>a;
		A.push_back(a);
		a_cur += a;
		b_cur += ~a;
		A_CSA.push_back(a_cur);
		B_CSA.push_back(b_cur);
	}
	ll mx = 0;
	for(int i= 0; i < N+1; i++) {
		for(int j = i; j < N+1; j++) {
			mx = max(mx, (j-i)+(B_CSA[j]-B_CSA[i])-(A_CSA[j]-A_CSA[i]));
		}
	}
	cout<<A_CSA[N]+mx<<endl;
}

int main() {
	int T;
	cin>>T;
	for(int i = 0; i < T; i++) {
		solve();
	}
	return 0;
}