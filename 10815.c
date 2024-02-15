/*
문제
숫자 카드는 정수 하나가 적혀져 있는 카드이다. 우리는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 우리가 가지고 있는지 아닌지를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 우리가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다. 두 숫자 카드에 같은 수가 적혀있는 경우는 없다.

셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 넷째 줄에는 우리가 가지고 있는 숫자 카드인지 아닌지를 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다. 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다

출력
첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 우리가 가지고 있으면 1을, 아니면 0을 공백으로 구분해 출력한다.
*/

#include <stdio.h>
#include <stdlib.h>
//#define SIZE 500000
//int a[SIZE];
//int b[SIZE];

int compare(const void *a, const void *b) {
    return *(int *)a - *(int *)b;
}

int binarySearch(int a[], int L, int R, int target){
    int m;
    while(L <= R){
        m = (L+R)/2;
        if(a[m] == target){
            return m;
        }else if(a[m] > target){
            R = m-1;
        }else{
            L = m+1;
        }
    }
    return -1;
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
        if(binarySearch(a, 0, N-1, b[i])!=-1){
            printf("1 ");
        }else{
            printf("0 ");
        }
    }
    
    free(a);
    free(b);
    return 0;
}
