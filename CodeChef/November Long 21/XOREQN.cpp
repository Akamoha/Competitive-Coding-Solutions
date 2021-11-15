#include<bits/stdc++.h>
#define pb push_back
#define fr(i,j,k,d) for(int i=j; i<k; i+=d)
#define X 60
#define MXN 1000000
#define MXNSMALL 1000
using namespace std;

void solveLarge(int N) {
	long long int inp;
	vector<bitset<X> > I;
	fr(i, 0, N, 1) {
		cin>>inp;
		bitset<X> A{inp};
		I.pb(A);
	}
	vector<bitset<MXN> > T;
	fr(i, 0, X, 1) {
		bitset<MXN> dummy;
		T.pb(dummy);
	}
	fr(i, 0, X, 1) {
		fr(j, 0, N, 1) {
			T[i][j] = I[j][i];
		}
	}
	bitset<MXN> carry;
	bitset<MXN> res;
	bitset<X> ans;
	for(int i=0; i<X; i++) {
		res = T[i] ^ carry;
		carry = T[i] & carry;
		if(res.count()%2) {
			carry = carry | res;
			ans[i] = 1;
		}
	}
	if(ans[X-1]) {
		cout<<"-1\n";
	} else {
		cout<<ans.to_ulong()<<"\n";
	}
}

void solveSmall(int N) {
	long long int inp;
	vector<bitset<X> > I;
	fr(i, 0, N, 1) {
		cin>>inp;
		bitset<X> A{inp};
		I.pb(A);
	}
	vector<bitset<MXNSMALL> > T;
	fr(i, 0, X, 1) {
		bitset<MXNSMALL> dummy;
		T.pb(dummy);
	}
	fr(i, 0, X, 1) {
		fr(j, 0, N, 1) {
			T[i][j] = I[j][i];
		}
	}
	bitset<MXNSMALL> carry;
	bitset<MXNSMALL> res;
	bitset<X> ans;
	for(int i=0; i<X; i++) {
		res = T[i] ^ carry;
		carry = T[i] & carry;
		if(res.count()%2) {
			carry = carry | res;
			ans[i] = 1;
		}
	}
	if(ans[X-1]) {
		cout<<"-1\n";
	} else {
		cout<<ans.to_ulong()<<"\n";
	}
}

int main() {
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);  
	
	int t, N;
	cin>>t;
	while(t--) {
		cin>>N;
		if(N>1000)
			solveLarge(N);
		else
			solveSmall(N);
	}
	return 0;
}