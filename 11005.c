/*
문제
10진법 수 N이 주어진다. 이 수를 B진법으로 바꿔 출력하는 프로그램을 작성하시오.

10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.

A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35

입력
첫째 줄에 N과 B가 주어진다. (2 ≤ B ≤ 36) N은 10억보다 작거나 같은 자연수이다.

출력
첫째 줄에 10진법 수 N을 B진법으로 출력한다.
 */

#include <stdio.h>

#define SIZE 1000

int main(){
    int N; // Number
    int B; // Base
    int quotient;
    int remainder;
    int n[SIZE] = {0}; // Numeric
    int digits = 0;
    char ch;

    scanf("%d %d", &N, &B);

    //printf("%d, %d", N, B);

    quotient = N;
    remainder = B;
    for(int i=0;quotient>0;i++){
        remainder = quotient%B; 
        quotient = quotient/B;
        n[i] = remainder;
        digits++;
        //printf("%d\n", n[i]);
    }

    for(int i=digits-1;i>=0;i--){
        ch = n[i];

        if(ch >= 10){
            ch = 'A' + (n[i]-10);
        }else if(ch <= 9 && ch >= 0){
            ch = '0' + n[i];
        }

        printf("%c", (char)ch);
    }

    return 0;
}