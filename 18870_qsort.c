/*
문제
수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다. Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표 Xj의 개수와 같아야 한다. X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.

입력
첫째 줄에 N이 주어진다. 둘째 줄에는 공백 한 칸으로 구분된 X1, X2, ..., XN이 주어진다.

출력
첫째 줄에 X'1, X'2, ..., X'N을 공백 한 칸으로 구분해서 출력한다.
*/

#include <stdio.h>
#include <stdlib.h>

int compare0(const void *a, const void *b) {
    const int *numA = *(const int **)a;
    const int *numB = *(const int **)b;
    if(numA[0] > numB[0]) return 1;
    else if(numA[0] < numB[0]) return -1;
    else return 0;
}

int compare1(const void *a, const void *b) {
    const int *numA = *(const int **)a;
    const int *numB = *(const int **)b;
    if(numA[1] > numB[1]) return 1;
    else if(numA[1] < numB[1]) return -1;
    else return 0;
}

int main(){
    int N;
    scanf("%d", &N);

    int **x = (int **)malloc(N * sizeof(int *));
    for (int i = 0; i < N; i++) {
        x[i] = (int *)malloc(2 * sizeof(int));
    }

    for(int i=0;i<N;i++){
        x[i][0] = i;
        scanf("%d", &x[i][1]);
    }

    qsort(x, N, sizeof(x[0]), compare1);

    int cnt = 0;
    for(int i = 0;i<N-1;i++) {
        if (x[i][1] != x[i+1][1]) {
            x[i][1] = cnt;
            cnt++;
        } else {
            x[i][1] = cnt;
        }
    }
    x[N - 1][1] = cnt;

    qsort(x, N, sizeof(x[0]), compare0);

    for(int i=0;i<N;i++){
        printf("%d ", x[i][1]);
    }

    // Free the dynamically allocated memory
    for (int i = 0; i < N; i++) {
        free(x[i]);
    }
    free(x);

    return 0;
}