/*
문제
예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

입력
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

출력
첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.
 */

#include <stdio.h>

int main(){
    int N;

    scanf("%d", &N);

    for(int i=0;i<N;i++){
        for(int k=1;k<N-i;k++) printf(" ");
        for(int j=0;j<2*i+1;j++) printf("*");
        printf("\n");
    }
    for(int i=N-2;i>=0;i--){
        for(int k=1;k<N-i;k++) printf(" ");
        for(int j=0;j<2*i+1;j++) printf("*");
        printf("\n");
    }

    return 0;
}