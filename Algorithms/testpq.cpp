/*
*	Some code I wrote to test the
*	behaviour of a priority queue
*	as a min heap and a max heap.
*/

#include<bits/stdc++.h>

#define ll long long int
#define sll(x) scanf("%lld", &x)
#define mp make_pair

using namespace std;

typedef pair<pair<ll, ll>, ll> tuple;

int main() {
	priority_queue<tuple, vector<tuple>, greater<tuple> > q;
	ll N, i, a, b, c;
	sll(N);
	for(i = 0; i < N; i++) {
		sll(a); sll(b); sll(c);
		q.push(mp(mp(a, b), c));
	}
	while(!q.empty()) {
		tuple values = q.top(); q.pop();
		a = values.first.first;
		b = values.first.second;
		c = values.second;
		printf("%lld %lld %lld\n", a, b, c);
	}
	return 0;
}