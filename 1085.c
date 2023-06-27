/*
문제
한수는 지금 (x, y)에 있다. 직사각형은 각 변이 좌표축에 평행하고, 왼쪽 아래 꼭짓점은 (0, 0), 오른쪽 위 꼭짓점은 (w, h)에 있다. 직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 x, y, w, h가 주어진다.

출력
첫째 줄에 문제의 정답을 출력한다.
 */

#include <stdio.h>

int getMin(int n1, int n2, int n3, int n4){
    int a[] = {n2, n3, n4};
    int min = n1;
    for(int i=0;i<3;i++){
        if(a[i] < min) min = a[i]; 
    }
    return min;
}

int main(void){
    int x, y, w, h;
    scanf("%d %d %d %d", &x, &y, &w, &h);
    printf("%d", getMin(x, y, w-x, h-y));
    return 0;
}