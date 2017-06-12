#include <stdio.h>
#include <iostream>
#include <vector>
 
using namespace std;
 
int main () {

	int T, t, N, K, i, leni, j, k, element, bittoset, bmpindex, ans;
	bool flag;
	vector<long> bmp, bmpcheck;
	vector<vector<long> > Nbmps;

	for(i = 0; i < 79; i++) {
		bmpcheck.push_back(0);
		bmp.push_back(0);
	}

	cin>>T;
	for(t = 0; t < T; t++) {
		cin>>N>>K;

		bmpcheck.clear();
		for(i = 0; i < 79; i++) {
			bmpcheck.push_back(0);
		}

		Nbmps.clear();
		for(i = 1; i <= K; i++) {
			bmpindex = 78 - (i-1)/32;
			bittoset = (i-1)-32*((i-1)/32);
			bmpcheck[bmpindex] |= 1<<bittoset;
		}

		for(i = 0; i < N; i++) {
			Nbmps.push_back(bmp);
			cin>>leni;
			for(j = 0; j < leni; j++) {
				cin>>element;
				bmpindex = 78 - (element-1)/32;
				bittoset = (element-1)-32*((element-1)/32);
				Nbmps[i][bmpindex] |= 1<<bittoset;
			}
		}
		
		ans = 0;
		for(i = 0; i < N; i++) {
			for(j = i+1; j < N; j++) {
				flag = true;
				for(k = 78; k >= 0; k--) {
					if((Nbmps[i][k] | Nbmps[j][k]) != bmpcheck[k]) {
						flag = false;
						break;
					}
				}
				if(flag) {
					ans += 1;
				}
			}
		}
		cout<<ans<<endl;
	}
	return 0;
}  
