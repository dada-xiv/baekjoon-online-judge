/*
문제
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

입력
첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

출력
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
 */

#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define MAX 1000000
#define SIZE 26

char getMostUsed(char used[], int usedN[], int usedLen){
    int maxN;
    int maxIdx;
    int maxIdxF;
    int maxIdxB;

    maxN = usedN[0];
    maxIdx = 0;
    for(int i=1;i<usedLen;i++){
        if(usedN[i]>maxN){
            maxN = usedN[i];
            maxIdx = i;
        }
    }

    maxIdxF = maxIdx;

    maxN = usedN[usedLen-1];
    maxIdx = usedLen-1;
    for(int i=usedLen-1;i>=0;i--){
        if(usedN[i]>maxN){
            maxN = usedN[i];
            maxIdx = i;
        }
    }

    maxIdxB = maxIdx;

    if(maxIdxB==maxIdxF)
        return used[maxIdx];
    else
        return '?';

}

int main(){
    char str[MAX];
    char used[SIZE];
    int usedN[SIZE];
    int strLen;
    int usedLen;
    int isMatch = 0;

    scanf("%s", str);

    strLen = strlen(str);

    for(int i=0;i<strLen;i++){
        str[i] = (char)toupper(str[i]);
    }

    //printf("%s\n", str);

    usedLen = 0;
    for(int i=0;i<strLen;i++){
        isMatch = 0;
        for(int j=0;j<usedLen;j++){
            if(str[i] == used[j]){
                isMatch = 1;
                usedN[j] += 1;
                break;
            }
        }
        if(isMatch == 0){
            used[usedLen] = str[i];
            usedN[usedLen] = 1;
            usedLen++;
        }
    }

    /*
    for(int i=0;i<usedLen;i++){
        printf("[%c:%d]", used[i],usedN[i]);
    }
    printf("\n");
    */

    printf("%c\n", getMostUsed(used, usedN, usedLen));

    return 0;
}