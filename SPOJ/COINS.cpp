#include<iostream>
#include<stdio.h>
#include<map>

using namespace std;

std::map <long long, long long>::iterator hm1_iter;
std::map <long long, long long> hm1;
typedef pair<long long, long long> Int_Pair;

long long max(long long a, long long b) {
	if(a > b) {
		return a;
	}
	return b;
}

long long f(long long N) {
	if (hm1.find(N) == hm1.end()) {
		hm1[N] = max(N, f(N/2) + f(N/3) + f(N/4));
	}
	return hm1[N];
}

int main() {
	hm1.insert(Int_Pair(1, 1));
	hm1.insert(Int_Pair(2, 2));
	hm1.insert(Int_Pair(3, 3));
	hm1.insert(Int_Pair(4, 4));
	long long N;
	while(scanf("%lld", &N) == 1) {
		cout<<f(N)<<endl;
	}
	return 0;
}