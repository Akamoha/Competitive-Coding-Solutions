#include<stdio.h>
#include<iostream>
#include<bits/stdc++.h>

#define sd(x) scanf("%d", &x);
#define slld(x) scanf("%lld", &x);
#define print(x) printf("%lld\n", x);
#define TYPE long long int

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
	makeSet(1);
	makeSet(2);
	makeSet(3);
	makeSet(4);
	makeSet(5);
	makeSet(6);
	makeSet(7);
	
	unionFunc(1, 2);
	unionFunc(2, 3);
	unionFunc(4, 5);
	unionFunc(6, 7);
	unionFunc(5, 6);
	unionFunc(3, 7);
	
	print(findSet(1));
	print(findSet(2));
	print(findSet(3));
	print(findSet(4));
	print(findSet(5));
	print(findSet(6));
	print(findSet(7));
	return 0;
}