#include<stdio.h>
#include<iostream>
#include<bits/stdc++.h>

#define slld(x) scanf("%lld", &x);
#define ll long long int

using namespace std;

int main() {
	ll T, t, n, m, i, cash, answer;
	slld(T);
	vector<ll> wallets;
	for(t = 0; t < T; t++) {
		slld(n); slld(m);
		wallets.clear();
		answer = 0;
		for(i = 0; i < n; i++) {
			slld(cash);
			wallets.push_back(cash);
		}
		sort(wallets.begin(), wallets.end());
		for(i = 0; i < n; i++) {
			answer += (upper_bound(wallets.begin()+i+1, wallets.end(), m-wallets[i]) - lower_bound(wallets.begin()+i+1, wallets.end(), m-wallets[i]));
		}
		printf("%lld\n", answer);
	}
	
	return 0;
}