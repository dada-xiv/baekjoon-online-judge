/*
문제
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 A와 B가 주어진다. (0 < A,B < 1010000)

출력
첫째 줄에 A+B를 출력한다.
*/

/* FALSE :
#include <stdio.h>

int main(){
    unsigned long long int A;
    unsigned long long int B;
    unsigned long long int res;
    
    scanf("%llu %llu", &A, &B);

    res = A + B;

    printf("%llu", res);

    return 0;
}
*/

#include <stdio.h>

#define MAX 10000

int main(){
    int A[MAX];
    int B[MAX];

    scanf("%s %s", A, B);

    printf("%s, %s", A, B);

    return 0;
}
