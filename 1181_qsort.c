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
#include <stdlib.h>
#include <string.h>

#define SIZE 51

int compareStrings(const void *a, const void *b) {
    return strcmp((const char *)a, (const char *)b);
}


int compare(const void *a, const void *b){
    int lenA = strlen((const char *)a);
    int lenB = strlen((const char *)b);
    
    if(strcmp((const char *)a, (const char *)b) == 0){
        return 0;
    }else if(lenA < lenB || (lenA==lenB && strcmp((const char *)a, (const char *)b) < 0)){
        return -1;
    }else{
        return 1;
    }
}

int main(){
    int N;
    scanf("%d", &N);
    char a[N][SIZE];

    for(int i=0;i<N;i++){
        scanf("%s", a[i]);
    }

    qsort(a, N, SIZE, compare);

    for(int i=0;i<N-1;i++){
        if(strcmp(a[i],a[i+1])!=0)
            printf("%s\n", a[i]);
    }
    printf("%s\n", a[N-1]);
    return 0;
}