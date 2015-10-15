#include<stdio.h>
#include<iostream>
#include<map>
using namespace std;

int main() {
	long long int T, t, n, i, num, flag, ans;
	map<long long int, long long int> HT;
	scanf("%lld", &T);
	for(t = 0; t < T; t++) {
		flag = 0;
		ans = 0;
		HT.clear();
		scanf("%lld", &n);
		for(i = 0; i < n; i++) {
			scanf("%lld", &num);
			if(HT.find(num) == HT.end()) {
				HT[num] = 1;
				if(HT[num] > n/2) {
					ans = num;
					flag = 1;
				}
			} else {
				HT[num] += 1;
				if(HT[num] > n/2) {
					ans = num;
					flag = 1;
				}
			}
		}
		if(flag == 0) {
			printf("%s\n", "NO");
		} else {
			printf("%s %d\n", "YES", ans);
		}
	}
	return 0;
}