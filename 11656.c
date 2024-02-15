/*
문제
접미사 배열은 문자열 S의 모든 접미사를 사전순으로 정렬해 놓은 배열이다.

baekjoon의 접미사는 baekjoon, aekjoon, ekjoon, kjoon, joon, oon, on, n 으로 총 8가지가 있고, 이를 사전순으로 정렬하면, aekjoon, baekjoon, ekjoon, joon, kjoon, n, on, oon이 된다.

문자열 S가 주어졌을 때, 모든 접미사를 사전순으로 정렬한 다음 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 문자열 S가 주어진다. S는 알파벳 소문자로만 이루어져 있고, 길이는 1,000보다 작거나 같다.

출력
첫째 줄부터 S의 접미사를 사전순으로 한 줄에 하나씩 출력한다.
*/

#include <stdio.h>
#include <string.h>
#define SIZE 1001

void bubbleSort(char a[][SIZE], int n){
    char temp[SIZE];
    for(int i=0;i<n-1;i++){
        for(int j=0;j<n-i-1;j++){
            if(strcmp(a[j], a[j+1]) > 0){
                strcpy(temp, a[j]);
                strcpy(a[j], a[j+1]);
                strcpy(a[j+1], temp);
            }
        }
    }
}

int main(){
    char s[SIZE];
    scanf("%s", s);

    int n = strlen(s);
    char a[n][SIZE];

    for(int i=0;i<n;i++){
        strncpy(a[i], s+i, n-i+1);
    }

    bubbleSort(a, n);
    for(int i=0;i<n;i++){
        printf("%s\n", a[i]);
    }
    return 0;
}