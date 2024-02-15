/*
문제
그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 단어가 들어온다. 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.

출력
첫째 줄에 그룹 단어의 개수를 출력한다.
 */

#include <stdio.h>
#include <string.h>

#define MAX 100
#define SIZE 100

int isGroupWord(char st[], int stLen){
    //int stLen;
    char chBuff[SIZE];
    char ch;
    int buffIdx;
    int isOverlap = 0;

    //stLen = strlen(st);

    buffIdx = 0;
    ch = ' ';
    for(int i=0;i<stLen;i++){
        if(st[i]!=ch){
            for(int j=0;j<buffIdx;j++){
                if(chBuff[j]==st[i]){
                    isOverlap = 1;
                    break;
                }
            }
            if(isOverlap == 0){
                chBuff[buffIdx] = st[i];
                ch = st[i];
                buffIdx++;
            }
        }
    }
    
    /* Debug
    for(int i=0;i<buffIdx;i++){
        printf("%c", chBuff[i]);
    }
    printf("\n");
    */

    return !isOverlap;
}

int main(){
    char st[SIZE];
    int N; // Number of inputs
    int totalGroupWord = 0;
    int stLen;
    int isGrpWrd;

    scanf("%d", &N);

    for(int i=0;i<N;i++){
        scanf("%s", st);
        stLen = strlen(st);

        isGrpWrd = isGroupWord(st, stLen);
        totalGroupWord += isGrpWrd;

        //printf("%d: (%d) %s\n", i, isGrpWrd, st);
    }

    printf("%d", totalGroupWord);

    return 0;
}