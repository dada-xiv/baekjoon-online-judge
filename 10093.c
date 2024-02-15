/*
문제
두 양의 정수가 주어졌을 때, 두 수 사이에 있는 정수를 모두 출력하는 프로그램을 작성하시오.

입력
두 정수 A와 B가 주어진다.

출력
첫째 줄에 두 수 사이에 있는 수의 개수를 출력한다.

둘째 줄에는 두 수 사이에 있는 수를 오름차순으로 출력한다.

서브태스크
번호	배점	제한
1	30	1 ≤ A, B ≤ 1000.
2	70	1 ≤ A, B ≤ 1015, A와 B의 차이는 최대 100,000.
*/

#include <stdio.h>

int main(){
    long long int A, B;
    long long int tmp;
    long long int diff;

    scanf("%lld %lld", &A, &B);

    if(A>B){
        tmp = A;
        A = B;
        B = tmp;
    }

    diff = B-A-1;

    if(diff > 0){
        printf("%lld\n", diff);

        long long int i;
        for(i=1;i<=diff;i++){
            printf("%lld ", A+i);
        }
    }else{
        printf("0");
    }

    return 0;
}