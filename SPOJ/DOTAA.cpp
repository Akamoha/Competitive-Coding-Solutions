#include<stdio.h>
#include<iostream>

using namespace std;

int main() {
	int T, m, n, D, t, ele, i, c;
	cin>>T;
	for(t = 0; t < T; t++) {
		cin>>n>>m>>D;
		c = 0;
		for(i = 0; i < n; i++) {
			cin>>ele;
			if(1.0*ele/D > (int)(ele/D)) {
				c += ele/D;
			} else if(1.0*ele/D == (int)ele/D) {
				c += ele/D - 1;
			}
		}
		if(c >= m) {
			cout<<"YES"<<endl;
		} 
		else {
			cout<<"NO"<<endl;
		}
	}
}