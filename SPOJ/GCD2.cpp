#include<stdio.h>
#include<iostream>
#include<string>

using namespace std;

int gcd(int a, int b) {
	if (b==0)
		return a;
	else
		return gcd(b,a%b);
}

int main() {
	int T, t, A, i, B[251], BmodA, d;
	string Bc;
	char blank;
	cin>>T;
	getline(cin, Bc);
	for(t = 0; t < T; t++) {
		scanf("%d", &A);
		scanf("%c", &blank);
		getline(cin, Bc);
		d = 0;
		if(A == 0) {
			cout<<Bc<<endl;
			continue;
		}
		for(string::iterator it = Bc.begin(); it != Bc.end(); ++it) {
			d = (d*10+ (int)(*it - '0'))%A;
		}
		BmodA = d;
		cout<<gcd(A, BmodA)<<endl;
	}
	return 0;
}