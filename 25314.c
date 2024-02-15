/*
입력
첫 번째 줄에는 문제의 정수 $N$이 주어진다. $(4 \le N \le 1000$; $N$은 $4$의 배수$)$ 

출력
혜아가 $N$바이트 정수까지 저장할 수 있다고 생각하는 정수 자료형의 이름을 출력하여라.
 */

#include <stdio.h>

int main(void){
    int num;
    int n;

    scanf("%d", &num);

    n = num/4;

    for(int i=0;i<n;i++){
        printf("long ");
    }

    printf("int");
    
    return 0;
}