/*
문제
영어 대소문자와 공백으로 이루어진 문자열이 주어진다. 이 문자열에는 몇 개의 단어가 있을까? 이를 구하는 프로그램을 작성하시오. 단, 한 단어가 여러 번 등장하면 등장한 횟수만큼 모두 세어야 한다.

입력
첫 줄에 영어 대소문자와 공백으로 이루어진 문자열이 주어진다. 이 문자열의 길이는 1,000,000을 넘지 않는다. 단어는 공백 한 개로 구분되며, 공백이 연속해서 나오는 경우는 없다. 또한 문자열은 공백으로 시작하거나 끝날 수 있다.

출력
첫째 줄에 단어의 개수를 출력한다.
 */

#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define LEN 1000005

int countWords(const char* str){
    int lenStr = strlen(str);
    int isWordStart = 0;
    int count = 0;

    for(int i=0;i<lenStr;i++){
        if(!isspace(str[i]) && !isWordStart){
            isWordStart = 1;
            count++;
        }else if(isspace(str[i])){
            isWordStart = 0;
        }
    }

    return count;
}

int main(void){
    char str[LEN];
    int strLen;
    int count; // Number of words

    fgets(str, sizeof(str), stdin);

    strLen = strlen(str);

    count = countWords(str);
    printf("%d", count);

    return 0;
}