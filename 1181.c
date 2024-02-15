/*
문제
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

길이가 짧은 것부터
길이가 같으면 사전 순으로
단, 중복된 단어는 하나만 남기고 제거해야 한다.

입력
첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 주어지는 문자열의 길이는 50을 넘지 않는다.

출력
조건에 따라 정렬하여 단어들을 출력한다.
*/

#include <stdio.h>
#include <string.h>

#define SIZE 51

void merge(char a[][SIZE], int left, int mid, int right){
    int pivotL = left;
    int pivotR = mid + 1;
    int k = left;
    int n = right-left+1;
    char sorted[n][SIZE];

    while(pivotL<=mid && pivotR<=right){
        if(strlen(a[pivotL]) < strlen(a[pivotR]) || (strlen(a[pivotL]) == strlen(a[pivotR]) && strcmp(a[pivotL], a[pivotR]) < 0)){
            strcpy(sorted[k-left], a[pivotL]);
            k++;
            pivotL++;
        }else{
            strcpy(sorted[k-left], a[pivotR]);
            k++;
            pivotR++;
        }
    }

    // Copy the remaining elements
    while(pivotL <= mid){
        strcpy(sorted[k-left], a[pivotL]);
        k++;
        pivotL++;
    }

    while(pivotR <= right){
        strcpy(sorted[k-left], a[pivotR]);
        k++;
        pivotR++;
    }

    // Copy the sorted result into the array
    for(int i=left;i<=right;i++){
        strcpy(a[i], sorted[i-left]);
    }
}

void mergeSort(char a[][SIZE], int left, int right){
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
    char a[N][SIZE];

    for(int i=0;i<N;i++){
        scanf("%s", a[i]);
    }

    mergeSort(a, 0, N-1);

    for(int i=0;i<N-1;i++){
        if(strcmp(a[i],a[i+1])!=0)
            printf("%s\n", a[i]);
    }
    printf("%s\n", a[N-1]);
    return 0;
}