/*
문제
정수 A, B 가 주어진다. 세로 길이가 A cm, 가로 길이가 B cm 인 직사각형의 넓이를 cm2 단위로 구하시오.
 */

#include <stdio.h>

int main(void){
    int A, B;
    
    scanf("%d", &A);
    scanf("%d", &B);

    printf("%d", A*B);

    return 0;
}