/*
문제
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 A와 B가 주어진다. (0 < A,B < 10^10000)

출력
첫째 줄에 A+B를 출력한다.
*/

#include <stdio.h>
#include <string.h>

#define MAX 100002

int getMax(int a, int b){
    if(a > b) return a;
    else return b;
}

int main(){
    char A[MAX];
    char B[MAX];

    int lenA, lenB, len;

    int a[MAX] = {0};
    int b[MAX] = {0};
    int r[MAX] = {0};

    int tmp;

    scanf("%s %s", A, B);

    lenA = strlen(A);
    lenB = strlen(B);
    len = getMax(lenA, lenB);
    
    //printf("max len : %d\n", len);

    for(int i=lenA-1;i>=0;i--){
        a[i] = A[lenA-1-i] - '0';
    }
    for(int i=lenB-1;i>=0;i--){
        b[i] = B[lenB-1-i] - '0';
    }

    for(int i=0;i<len;i++){
        tmp = a[i]+b[i];
        if(tmp<10){
            r[i] = r[i] + tmp;
        }else{
            r[i] = r[i] + tmp - 10;
            r[i+1] = r[i+1] + 1;
            if(i+1==len) len++;
        }
    }

    //for(int i=len-1;i>=0;i--){printf("%d ",a[i]);}printf("\n");
    //for(int i=len-1;i>=0;i--){printf("%d ",b[i]);}printf("\n");
    for(int i=len-1;i>=0;i--) printf("%d",r[i]);

    return 0;
}
