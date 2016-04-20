#include<iostream>
#include<stdio.h>
#include<bits/stdc++.h>

#define TYPE long long int
#define sd(x) scanf("%d", &x);
#define slld(x) scanf("%lld", &x);
#define print(x) printf("%lld\n", x);

using namespace std;

struct node { 
	TYPE data;
	node* parent;
	TYPE rank;
};

map<TYPE, node*> M;

void makeSet(TYPE data) {
	node* newNode = new node();
	newNode->data = data;
	newNode->parent = newNode;
	newNode->rank = 0;
	M[data] = newNode;
}

node* findSet(node* n) {
	node* parent = n->parent;
	if(parent == n) {
		return parent;
	}
	n->parent = findSet(n->parent);
	return n->parent;
}

TYPE findSet(TYPE data) {
	return findSet(M[data])->data;
}

bool unionFunc(TYPE data1, TYPE data2) {
	node* n1 = M[data1];
	node* n2 = M[data2];
	node* parent1 = findSet(n1);
	node* parent2 = findSet(n2);
	
	if(parent1->data == parent2->data) {
		return false;
	}
	if(parent1->rank == parent2->rank) {
		parent1->rank++;
		parent2->parent = parent1;
	} else if(parent1->rank > parent2->rank) {
		parent2->parent = parent1;
	} else {
		parent1->parent = parent2;
	}
	return true;
}

int main() {
	TYPE t, tc, p, n, m, a, b, c, i, answer = 0;
	slld(t);
	for(tc = 0; tc < t; tc++) {
		slld(p); slld(n); slld(m);
		vector<pair<int, pair<int, int> > > edges;
		for(i = 0; i < m; i++) {
			slld(a); slld(b); slld(c);
			edges.push_back(make_pair(c, make_pair(a, b)));
			makeSet(a);
			makeSet(b);
		}
		sort(edges.begin(), edges.end());
		for(i = 0; i < m; i++) {
			TYPE root1 = findSet(edges[i].second.first);
			TYPE root2 = findSet(edges[i].second.second);
			if(root1 == root2) {
				continue;
			} else {
				unionFunc(root1, root2);
				answer += edges[i].first;
			}
		}
		print(answer*p);
	}
	return 0;
}