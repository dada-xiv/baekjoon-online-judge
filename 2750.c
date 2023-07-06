/*
문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

예제 입력 1 
10
5
6
4
7
3
1
8
2
9
0
*/

#include <stdio.h>

int main(){
    int N; // 1 ~ 10,000
    scanf("%d", &N);
    int a[N];
    for(int i=0;i<N;i++){
        scanf("%d", &a[i]);
    }

    int min;
    for(int i=0;i<N-1;i++){
        min = a[i];
        for(int j=i+1;j<N;j++){
            if(a[j] < min){
                a[i] = a[j];
                a[j] = min;
                min = a[i]; // New a[i] is the smallest
            }
        }
    }

    for(int k=0;k<N;k++){
        printf("%d\n", a[k]);
    }

    return 0;
}
