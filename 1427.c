/*
문제
수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.

입력
첫째 줄에 정렬하려고 하는 수 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력한다.
*/

#include <stdio.h>
#include <string.h>
#define SIZE 10

int main() {
    char val[10];
    int crr[SIZE] = {0};
    int num;
    
    scanf("%s", val);
    int len = strlen(val);

    for(int i=0;i<len;i++){
        num = val[i] - '0';
        crr[num] += 1;
    }

    for(int i=SIZE-1;i>=0;i--){
        if(crr[i]==0) continue;
        for(int j=0;j<crr[i];j++){
            printf("%d", i);
        }
    }

    return 0;
}