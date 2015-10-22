#include<stdio.h>

using namespace std;

int main()
{
	int T = 1;
	while(1){
		char S[2001], ch;
		int top = 0, count = 0, i = 0;
		scanf("%s",S);
		if(S[0] == '-') {
			break;
		}
		while(S[i] != '\0') {
			ch = S[i];
			if(ch == '{')
				top++;
			else if(ch == '}' && top == 0) {
				count++;
				top++;
			}
			else {
				top--;
			}
			i++;
		}
		printf("%d. %d\n", T++, (top/2)+count);
	}
	return 0;
}