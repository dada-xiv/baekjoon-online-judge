/*
문제
2차원 평면 위의 점 N개가 주어진다. 좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. (-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.

출력
첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.
*/

#include <stdio.h>

void merge(int a[][2], int left, int mid, int right){
    int pivotL = left;
    int pivotR = mid + 1;
    int k = left;
    int n = right-left+1;
    int sorted[n][2];

    while(pivotL<=mid && pivotR<=right){
        if(a[pivotL][1] < a[pivotR][1] || (a[pivotL][1] == a[pivotR][1] && a[pivotL][0] < a[pivotR][0])){
            sorted[k-left][0] = a[pivotL][0];
            sorted[k-left][1] = a[pivotL][1];
            k++;
            pivotL++;
        }else{
            sorted[k-left][0] = a[pivotR][0];
            sorted[k-left][1] = a[pivotR][1];
            k++;
            pivotR++;
        }
    }

    // Copy the remaining elements
    while(pivotL <= mid){
        sorted[k-left][0] = a[pivotL][0];
        sorted[k-left][1] = a[pivotL][1];
        k++;
        pivotL++;
    }

    while(pivotR <= right){
        sorted[k-left][0] = a[pivotR][0];
        sorted[k-left][1] = a[pivotR][1];
        k++;
        pivotR++;
    }

    // Copy the sorted result into the array
    for(int i=left;i<=right;i++){
        a[i][0] = sorted[i-left][0];
        a[i][1] = sorted[i-left][1];
    }
}

void mergeSort(int a[][2], int left, int right){
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
    int a[N][2];

    for(int i=0;i<N;i++){
        scanf("%d %d", &a[i][0], &a[i][1]);
    }

    mergeSort(a, 0, N - 1);

    for(int i=0;i<N;i++){
        printf("%d %d\n", a[i][0], a[i][1]);
    }
    return 0;
}
