/*
문제
세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.

입력
세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.

출력
직사각형의 네 번째 점의 좌표를 출력한다.
 */

#include <stdio.h>

int getRare(int a, int b, int c){
    if(a==b){
        return c;
    }else if(a==c){
        return b;
    }else{
        return a;
    }
}

int main(void){
    int x, y;
    int a[3][2];
    int newX, newY;
    int cnt = 0;

    for(int i=0;i<3;i++){
        scanf("%d %d", &x, &y);
        a[i][0] = x;
        a[i][1] = y;
    }

    newX = getRare(a[0][0], a[1][0], a[2][0]);
    newY = getRare(a[0][1], a[1][1], a[2][1]);

    printf("%d %d", newX, newY);
    
    return 0;
}