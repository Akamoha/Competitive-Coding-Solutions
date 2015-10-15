#include<stdio.h>
#include<iostream>
#include<string>
using namespace std;

void merge(long long int *arr, long long int size1, long long int size2, long long int *inversions) {
    long long int temp[size1+size2];
    long long int ptr1=0, ptr2=0;

    while (ptr1+ptr2 < size1+size2) {
        if (ptr1 < size1 && arr[ptr1] <= arr[size1+ptr2] || ptr1 < size1 && ptr2 >= size2)
            temp[ptr1+ptr2] = arr[ptr1++];

        if (ptr2 < size2 && arr[size1+ptr2] < arr[ptr1] || ptr2 < size2 && ptr1 >= size1) {
            temp[ptr1+ptr2] = arr[size1+ptr2++];
            *inversions += size1-ptr1;
        }
    }

    for (long long int i=0; i < size1+size2; i++)
        arr[i] = temp[i];
}

void mergeSort(long long int *arr, long long int size, long long int* inversions) {
    if (size == 1)
        return;

    long long int size1 = size/2, size2 = size-size1;
    mergeSort(arr, size1, inversions);
    mergeSort(arr+size1, size2, inversions);
    merge(arr, size1, size2, inversions);
}

int main() {
	long long int T, t, N, i;
	string blank;
	cin>>T;
	for(t = 0; t < T; t++) {
		getline(cin, blank);
		cin>>N;
		long long int A[N];
		for(i = 0; i < N; i++) {
			cin>>A[i];
		}
		long long int count = 0;
		mergeSort(A, N, &count);
		cout<<count<<endl;
	}
	return 0;
}