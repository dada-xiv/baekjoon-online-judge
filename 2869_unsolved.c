/*
문제
땅 위에 달팽이가 있다. 이 달팽이는 높이가 V미터인 나무 막대를 올라갈 것이다.

달팽이는 낮에 A미터 올라갈 수 있다. 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다. 또, 정상에 올라간 후에는 미끄러지지 않는다.

달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 세 정수 A, B, V가 공백으로 구분되어서 주어진다. (1 ≤ B < A ≤ V ≤ 1,000,000,000)

출력
첫째 줄에 달팽이가 나무 막대를 모두 올라가는데 며칠이 걸리는지 출력한다.
 */

#include <stdio.h>

int main(){
    int A, B, V;
    int reach = 0;
    int perDay;
    int quotient;
    int remainder;

    scanf("%d %d %d", &A, &B, &V);

    perDay = A - B;

    quotient = V/perDay;
    remainder = V%perDay;

    printf("%d = %d day x %d + %d\n", V, quotient, perDay, remainder);
    if(remainder != 0){
        if(A >= V){
            printf("D-day : %d\n", 1);
        }else{
            printf("D-day : %d\n", quotient+1);
        }
    }else{
        if(quotient-perDay+A >= V){
            printf("!D-day : %d\n", quotient-A+perDay);
        }else{
            printf("D-day : %d\n", quotient);
        }
    }

    return 0;
}