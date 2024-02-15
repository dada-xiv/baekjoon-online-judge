/*
문제
세 정수 A, B, C가 주어진다. 이때, 두 번째로 큰 정수를 출력하는 프로그램을 작성하시오. 

입력
첫째 줄에 세 정수 A, B, C가 공백으로 구분되어 주어진다. (1 ≤ A, B, C ≤ 100)

출력
두 번째로 큰 정수를 출력한다.
*/

int compare(const void *a, const void *b){
    int num1 = *(int *)a;
    int num2 = *(int *)b;
    return num1-num2;
}

#include <stdio.h>
#include <stdlib.h>
#define SIZE 3
int main(){
    int a[SIZE];
    for(int i=0;i<SIZE;i++){
        scanf("%d", &a[i]);
    }

    qsort(a, SIZE, sizeof(int), compare);

    printf("%d", a[1]);

    return 0;
}
