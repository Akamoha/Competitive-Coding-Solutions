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
	int N, M, m, i, j, k;
	sd(N); sd(M);
	vector<pair<int, pair<int, int> > > edges;
	vector<pair<int, pair<int, int> > > MSTedges;
	long long int answer = 0;
	for(m = 0; m < M; m++) {
		sd(i); sd(j); sd(k);
		edges.push_back(make_pair(k, make_pair(i, j)));
		makeSet(i);
		makeSet(j);
	}
	sort(edges.begin(), edges.end());
	for(i = 0; i < edges.size(); i++) {
		TYPE root1 = findSet(edges[i].second.first);
		TYPE root2 = findSet(edges[i].second.second);
		if(root1 == root2) {
			continue;
		} else {
			MSTedges.push_back(edges[i]);
			unionFunc(root1, root2);
			answer += edges[i].first;
		}
	}
	print(answer);
	return 0;
}