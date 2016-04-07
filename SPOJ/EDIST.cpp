#include <iostream>
#include <string>
using namespace std;

int temp[3000][3000];

int min_funct(int ele1,int ele2, int ele3){
	if (ele1 < ele2){
		if (ele1 < ele3){
			return ele1;
			}
		else{
			return ele3;
		}
	}
	else{
		if(ele2 < ele3){
			return ele2;
		}
		else{
			return ele3;
		}
	}
}

int main(){
	string A,B;
	int i,j,t,lenA,lenB,T;
	cin>>T;
	getline(cin, A);
	for(t = 0; t < T; t++) {
		getline(cin,A);
		getline(cin,B);
		lenA = A.length();
		lenB = B.length();
		for(i = 0;i < (lenB + 1);i++){
			temp[i][0] = i;
		}
		for(j = 0;j < (lenA + 1);j++){
			temp[0][j] = j;
		}

		for(i = 1; i < lenB + 1; i++){
			for(j = 1; j < lenA + 1; j++){
				if(A[j-1] == B[i-1]){
					temp[i][j] = temp[i-1][j-1];
				}
				else{
					temp[i][j] = min_funct(temp[i-1][j-1] , temp[i-1][j] , temp[i][j-1]) + 1;
				}
			}
		}
		cout<<temp[lenB][lenA]<<endl;
	}
	return 0;
}