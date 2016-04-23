#include<stdio.h>
#include<iostream>
#include<bits/stdc++.h>

#define sd(x) scanf("%d", &x);
#define slld(x) scanf("%lld", &x);
#define print(x) printf("%lld\n", x);
#define TYPE int

using namespace std;

struct node {
	TYPE data;
	node* parent;
	int rank;
};

unordered_map<TYPE, node*> MAP;

void makeSet(TYPE data) {
	node* newNode = new node();
	newNode->data = data;
	newNode->parent = newNode;
	newNode->rank = 0;
	MAP[data] = newNode;
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
	return findSet(MAP[data])->data;
}

bool unionFunc(TYPE data1, TYPE data2) {
	node* n1 = MAP[data1];
	node* n2 = MAP[data2];
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
	int N, M, i, A, B;
	sd(N); sd(M);
	unordered_map<int, int> HT;
	unordered_map<int, int>::iterator it;
	vector<pair<int, int> > edges;
	for(i = 0; i < M; i++) {
		sd(A); sd(B);
		makeSet(A); makeSet(B);
		edges.push_back(make_pair(A, B));
		if(HT.find(A) == HT.end()) {
			HT[A] = 1;
		}
		if(HT.find(B) == HT.end()) {
			HT[B] = 1;
		}
	}
	for(i = 0; i < edges.size(); i++) {
		unionFunc(edges[i].first, edges[i].second);
	}
	int setnum;
	unordered_map<int, int> HT2;
	for(it = HT.begin(); it != HT.end(); it++) {
		setnum = findSet(it->first);
		if(HT2.find(setnum) == HT2.end())
			HT2[setnum] = 1;
	}
	printf("%d\n", HT2.size()+N-HT.size());
	return 0;
}