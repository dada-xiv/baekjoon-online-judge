/*
문제
Write a program that repeatedly reads two numbers n and k and prints all bit patterns of length n with k ones in descending order (when the bit patterns are considered as binary numbers). 

입력
You may assume that 30 ≥ n > 0, 8 > k ≥ 0, and n ≥ k. 

출력
The first number in the input gives the number of pairs n and k. The numbers n and k are separated by a single space. Leading zeroes in a bit pattern should be included. See the example below.
 */

#include <stdio.h>
#include <math.h>

void intToBinary(int num, int length) {
    if (num == 0) {
        printf("0");
        return;
    }

    char b[32];
    int i = 0;

    for(;i<length && num > 0;i++){
        b[length-i] = '0' + (num % 2);
        num = num / 2;
    }
    b[i+1] = '\0';

    printf("%s\n", b);
}


int main(void){
    int n, k;
    long long int num = 0;

    scanf("%d %d", &n, &k);

    for(int i=n-1;i>=n-k;i--){
        num += pow(2,i);
    }
    //printf("%lld", num);

    int N = num / 2;
    int printNum;
    for(int i=0;i<N;i++){
        printNum = num - 2*i;
        //printf("%lld\n", num-2*i);
        intToBinary(printNum, n);
    }

    return 0;
}