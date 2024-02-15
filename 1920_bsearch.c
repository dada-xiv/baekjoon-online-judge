/*
문제
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

출력
M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.

cf) compare 함수를 단순히 a에서 b를 빼는 것으로 구현하면 오버플로우가 날 가능성이 있다. int형은 최소 -2^31, 최대 2^31 - 1이기 때문에, a와 b의 차이는 최대 2^32 - 1입니다. 이런 수가 compare 함수에 들어가게 되면 오버플로우가 발생하여 잘못된 결과를 낼 수 있다.
*/

#include <stdio.h>
#include <stdlib.h>

// for both qsort() and bsearch()
int compare(const void *a, const void *b) {
    int numA = *(int *)a;
    int numB = *(int *)b;
    if(numA > numB) return 1;
    else if(numA < numB) return -1;
    else return 0;
}

int main(){
    int N, M;

    scanf("%d", &N);
    int *a = (int *)malloc(sizeof(int)*N);

    for(int i=0;i<N;i++){
        scanf("%d", &a[i]);
    }

    qsort(a, N, sizeof(int), compare);

    scanf("%d", &M);
    int *b = (int *)malloc(sizeof(int)*M);

    for(int i=0;i<M;i++){
        scanf("%d", &b[i]);
    }

    for(int i=0;i<M;i++){
        int *p = (int *)bsearch(&b[i], a, N, sizeof(int), compare);
        if(p!=NULL){
            printf("1\n");
        }else{
            printf("0\n");
        }
    }
    
    free(a);
    free(b);
    return 0;
}
