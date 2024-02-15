/*
문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
*/

#include <stdio.h>
#define SIZE 1000000
int sorted[SIZE]; // Global array for sorted result

void merge(int a[], int left, int mid, int right){
    int pivotL = left;
    int pivotR = mid + 1;
    int k = left;

    while(pivotL<=mid && pivotR<=right){
        if(a[pivotL] <= a[pivotR]){
            sorted[k++] = a[pivotL++];
        }else{
            sorted[k++] = a[pivotR++];
        }
    }

    // Copy the remaining elements
    if(pivotL<=mid){
        for(int i=pivotL;i<=mid;i++){
            sorted[k++] = a[i];
        }
    }else if(pivotR<=right){
        for(int i=pivotR;i<=right;i++){
            sorted[k++] = a[i];
        }
    }

    // Copy the sorted result into the array
    for(int i=left;i<=right;i++){
        a[i] = sorted[i];
    }
}

void mergeSort(int a[], int left, int right){
    int mid;

    if(left < right){
        mid = (left + right) / 2;
        mergeSort(a, left, mid);
        mergeSort(a, mid+1, right);
        merge(a, left, mid, right);        
    }
}

int main(){
    int N;
    scanf("%d", &N);

    int a[N];

    for(int i=0;i<N;i++){
        scanf("%d", &a[i]);
    }

    mergeSort(a, 0, N-1);

    for(int i=0;i<N;i++){
        printf("%d\n", a[i]);
    }

}