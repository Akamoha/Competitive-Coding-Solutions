#include<iostream>
#include<stdio.h>
#include<bits/stdc++.h>

#define sd(x) scanf("%d", &x)
#define slld(x) scanf("%lld", &x);
#define ll long long int
#define max(a,b) a>b?a:b
using namespace std;

vector<ll> heights;

ll ans(ll cutheight) {
	ll i;
	ll res = 0;
	for(i = 0; i < heights.size(); i++) {
		res += max(0, heights[i]-cutheight);
	}
	return res;
}

int main() {
	ll N, M, i, h, maxheight = -1;
	slld(N); slld(M);
	for(i = 0; i < N; i++) {
		slld(h);
		heights.push_back(h);
		if(maxheight < h)
			maxheight = h;
	}
	ll low = 0;
	ll high = maxheight;
	ll mid;
	ll wood;
	bool flag = true;
	while(low <= high) {
		mid = (low+high)/2;
		wood = ans(mid);
		if(wood == M) {
			printf("%lld\n", mid);
			flag = false;
			break;
		} else if(wood > M) {
			low = mid+1;
		} else {
			high = mid-1;
		}
	}
	if(flag)
		printf("%lld\n", high);
	return 0;
}