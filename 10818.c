/*
문제
N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다. 모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.

출력
첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.
 */

#include <stdio.h>
#include <stdlib.h>

#define SIZE 1000000

int findMax(int arr[], int size){
    int max = arr[0];

    for(int i=1;i<size;i++){
        if(arr[i]>max){
            max = arr[i];
        }
    }

    return max;
}

int findMin(int arr[], int size){
    int min = arr[0];

    for(int i=1;i<size;i++){
        if(arr[i]<min){
            min = arr[i];
        }
    }

    return min;
}

int main(void){
    int total;
    int i = 0;

    //int arr[SIZE];
    int* arr = (int*)malloc(SIZE*sizeof(int));

    scanf("%d", &total);

    while(scanf("%d", &arr[i]) != EOF && i<SIZE) {
        i++;
    }

    printf("%d %d", findMin(arr, i), findMax(arr, i));
    
    free(arr); // free the allocated memory
    return 0;
}