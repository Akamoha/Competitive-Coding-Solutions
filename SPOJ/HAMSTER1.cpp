#include<stdio.h>
#include<iostream>
#include<bits/stdc++.h>
#include<math.h>

#define sd(x) scanf("%d", &x)
#define PI 3.14159265358979323846264338327950

using namespace std;

double projectileHeight(int v0, double theta) {
	return v0*v0*sin(theta)*sin(theta)/20;
}

double projectileRange(int v0, double theta) {
	return v0*v0*sin(2*theta)/10;
}

pair<double, double> ans(int v0, int k1, int k2) {
	double theta = (PI - atan(4.0*k1/k2))/2;
	double H = projectileHeight(v0, theta);
	double R = projectileRange(v0, theta);
	return make_pair(theta, k1*R + k2*H);
}

int main() {
	int T, t, v0, k1, k2;
	pair<double, double> anstemp;
	sd(T);
	for(t = 0; t < T; t++) {
		sd(v0); sd(k1); sd(k2);
		anstemp = ans(v0, k1, k2);
		printf("%.3lf %.3lf\n", anstemp.first, anstemp.second);
	}
	return 0;
}