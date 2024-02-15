/*
문제
숫자 세 개가 주어졌을 때, 가장 작은 수, 그 다음 수, 가장 큰 수를 출력하는 프로그램을 작성하시오.

입력
숫자 세 개가 주어진다. 이 숫자는 1보다 크거나 같고, 1,000,000보다 작거나 같다. 이 숫자는 모두 다르다.

출력
제일 작은 수, 그 다음 수, 제일 큰 수를 차례대로 출력한다.
*/

#include <stdio.h>

int getMax(int a, int b, int c){
    if(a>b)
        return (a>c) ? a : c;
    else
        return (b>c) ? b : c;
}

int getMin(int a, int b, int c){
    if(a<b)
        return (a<c) ? a : c;
    else
        return (b<c) ? b : c;
}

int main(void){
    int a, b, c;
    int min, max, mid;

    scanf("%d %d %d", &a, &b, &c);

    max = getMax(a, b, c);
    min = getMin(a, b, c);
    mid = a+b+c-(max+min);

    printf("%d %d %d", min, mid, max);

    return 0;
}