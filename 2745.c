/*
문제
B진법 수 N이 주어진다. 이 수를 10진법으로 바꿔 출력하는 프로그램을 작성하시오.

10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.

A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35

입력
첫째 줄에 N과 B가 주어진다. (2 ≤ B ≤ 36)

B진법 수 N을 10진법으로 바꾸면, 항상 10억보다 작거나 같다.

출력
첫째 줄에 B진법 수 N을 10진법으로 출력한다.
 */

#include <stdio.h>
#include <string.h>
#include <math.h>

#define SIZEDIGIT 100

int main(){
    char nStr[SIZEDIGIT]; // Number string
    int N; // Number system
    int nLen; // Number of digits
    int nD;
    int sum = 0;

    scanf("%s %d", nStr, &N);
    nLen = strlen(nStr);

    for(int i=0;i<nLen;i++){

        nD = (int)nStr[i];
        if(nD >= 'A' && nD <= 'Z'){
            nD = nD - 'A' + 10;
        }else if(nD >= '0' && nD <= '9'){
            nD = nD - '0';
        }
        sum += nD * pow(N, nLen-i-1);
        //printf("%d x %d^%d\n", nD, N, nLen-i-1);
    }

    printf("%d", sum);

    return 0;
}