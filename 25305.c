/*
문제
N명의 학생들이 응시했다. 이들 중 점수가 가장 높은 k명은 상을 받을 것이다. 이 때, 상을 받는 커트라인이 몇 점인지 구하라. 커트라인이란 상을 받는 사람들 중 점수가 가장 가장 낮은 사람의 점수를 말한다.

입력
첫째 줄에는 응시자의 수 N과 상을 받는 사람의 수 k가 공백을 사이에 두고 주어진다.
둘째 줄에는 각 학생의 점수 x가 공백을 사이에 두고 주어진다.

출력
상을 받는 커트라인을 출력하라.

제한 
1 ≤ N ≤ 1,000
1 ≤ k ≤ N 
0 ≤ x ≤ 10,000
*/

#include <stdio.h>

int main(){
    int N, k;
    scanf("%d %d", &N, &k);
    int a[N];

    for(int i=0;i<N;i++){
        scanf("%d", &a[i]);
    }

    int max;
    for(int i=0;i<N-1;i++){
        max = a[i];
        for(int j=i+1;j<N;j++){
            if(a[j] > max){
                a[i] = a[j];
                a[j] = max;
                max = a[i]; // New a[i] is the greatest
            }
        }
    }

    printf("%d", a[k-1]);

    return 0;
}