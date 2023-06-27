/*
임씨의 이름이 새겨진 옥구슬이 나오는 모든 지점을 포함하는 가장 작은 남북, 동서 방향으로 평행한 변을 갖는 직사각형의 대지를 임씨의 소유로 인정한다.” 임씨는 많은 손해를 보는 셈이지만 더 이상을 요구할 만한 근거가 없었기 때문에 이 판결을 따르기로 했다.

입력
첫째 줄에는 점의 개수 N (1 ≤ N ≤ 100,000) 이 주어진다. 이어지는 N 줄에는 각 점의 좌표가 두 개의 정수로 한 줄에 하나씩 주어진다. 각각의 좌표는 -10,000 이상 10,000 이하의 정수이다. 

출력
첫째 줄에 N 개의 점을 둘러싸는 최소 크기의 직사각형의 넓이를 출력하시오. 
 */

#include <stdio.h>

int main(void){
    int Xmin, Xmax;
    int Ymin, Ymax;
    int x, y;
    int N;

    scanf("%d", &N);

    if(N==1){
        printf("0");
        return 0;
    }

    scanf("%d %d", &x, &y);
    
    Xmin = x; Xmax = x;
    Ymin = y; Ymax = y;

    for(int i=1;i<N;i++){
        scanf("%d %d", &x, &y);
        if(x < Xmin) Xmin = x;
        if(x > Xmax) Xmax = x;
        if(y < Ymin) Ymin = y;
        if(y > Ymax) Ymax = y;
    }

    printf("%d", (Xmax-Xmin)*(Ymax-Ymin));

    return 0;
}