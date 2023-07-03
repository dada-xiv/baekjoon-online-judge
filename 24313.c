/*
문제
알고리즘의 소요 시간을 나타내는 O-표기법(빅-오)을 다음과 같이 정의하자.

O(g(n)) = {f(n) | 모든 n ≥ n0에 대하여 f(n) ≤ c × g(n)인 양의 상수 c와 n0가 존재한다}

이 정의는 실제 O-표기법과 다를 수 있다.

함수 f(n) = a1n + a0, 양의 정수 c, n0가 주어질 경우 O(n) 정의를 만족하는지 알아보자.

입력
첫째 줄에 함수 f(n)을 나타내는 정수 a1, a0가 주어진다. (0 ≤ |ai| ≤ 100)

다음 줄에 양의 정수 c가 주어진다. (1 ≤ c ≤ 100)
다음 줄에 양의 정수 n0가 주어진다. (1 ≤ n0 ≤ 100)

출력
f(n), c, n0가 O(n) 정의를 만족하면 1, 아니면 0을 출력한다.


f(n) = 7n + 7, g(n) = n, c = 8, n0 = 1이면 f(1) = 14, c × g(1) = 8이므로 O(n) 정의를 만족하지 못한다.
*/

#include <stdio.h>

int main(){
    int a1, a0;
    int c, n0;
    double val;

    scanf("%d %d", &a1, &a0);
    scanf("%d", &c);
    scanf("%d", &n0);

    if(a1==c){
        if(a0 <= 0) printf("1");
        else printf("0");
    }else if(a1 > c){
        printf("0");
    }else{
        val = (double) a0/(c-a1);
        if (n0 >= val) printf("1");
        else printf("0");
    }

    return 0;
}