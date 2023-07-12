/*
문제
첫째 줄에는 별 2×N-1개, 둘째 줄에는 별 2×N-3개, ..., N번째 줄에는 별 1개를 찍는 문제

별은 가운데를 기준으로 대칭이어야 한다.

입력
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

출력
첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.
 */

#include <stdio.h>

int main(void){
    int N;

    scanf("%d", &N);

    for(int i=N;i>=1;i--){
        for(int j=0;j<=N-i;j++){
            printf("*");
        }
        for(int j=1;j<2*i-1;j++){
            printf(" ");
        }
        for(int j=0;j<=N-i;j++){
            printf("*");
        }
        printf("\n");
    }

    for(int i=2;i<=N;i++){
        for(int j=0;j<=N-i;j++){
            printf("*");
        }
        for(int j=1;j<2*i-1;j++){
            printf(" ");
        }
        for(int j=0;j<=N-i;j++){
            printf("*");
        }
        printf("\n");
    }

    return 0;
}