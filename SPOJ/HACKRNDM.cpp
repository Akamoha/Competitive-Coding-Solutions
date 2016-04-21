#include<stdio.h>
#include<iostream>
#include<bits/stdc++.h>
#include<unordered_map>

#define ll long long int
#define slld(x) scanf("%lld", &x);

using namespace std;

int main() {
	ll n, k, i, num;
	slld(n); slld(k);
	vector<ll> numbers;
	unordered_map<ll, ll> HT;
	for(i = 0; i < n; i++) {
		slld(num);
		numbers.push_back(num);
		if(HT.find(num) == HT.end())
			HT[num] = 1;
		else
			HT[num]++;
	}
	ll ans = 0;
	for(auto &it : HT) {
		if(HT.find(it.first+k) != HT.end()) {
			ans += HT.find(it.first+k)->second;
		}
	}
	printf("%lld\n", ans);
	return 0;
}