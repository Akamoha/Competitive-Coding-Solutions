#include<stdio.h>
#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main() {
	unsigned long long int N, i, ele, ans;
	while(1) {
		scanf("%llu", &N);
		if(N == 0) {
			break;
		}
		vector<unsigned long long int> C, P;
		for(i = 0; i < N; i++) {
			scanf("%llu", &ele);
			C.push_back(ele);
		}
		for(i = 0; i < N; i++) {
			scanf("%llu", &ele);
			P.push_back(ele);
		}
		ans = 0;
		sort(C.begin(), C.end());
		sort(P.begin(), P.end());
		for(vector<unsigned long long int>::iterator it = C.begin(); it != C.end(); it++) {
			ans += (*it) * *(P.end()-1);
			P.pop_back();
		}
		printf("%llu\n", ans);
	}
	return 0;
}