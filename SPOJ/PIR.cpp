#include<stdio.h>
#include<iostream>
#include<math.h>

using namespace std;

int main() {
	int T, t;
	double U, V, W, u, v, w;
	double a, b, c, d, x, y, z, X, Y, Z;
	scanf("%d", &T);
	for(t = 0; t < T; t++) {
		scanf("%lf %lf %lf %lf %lf %lf", &U, &V, &w, &W, &v, &u);
		X = (w - U + v)*(U + v + w);
		x = (U - v + w)*(v - w + U);
		Y = (u - V + w)*(V + w + u);
		y = (V - w + u)*(w - u + V);
		Z = (v - W + u)*(W + u + v);
		z = (W - u + v)*(u - v + W);
		a = sqrt(x*Y*Z);
		b = sqrt(y*Z*X);
		c = sqrt(z*X*Y);
		d = sqrt(x*y*z);
		printf("%.4lf\n", (sqrt((b-a+c+d)*(a-b+c+d)*(a+b-c+d)*(a+b+c-d)))/(192*u*v*w));
	}
	return 0;
}