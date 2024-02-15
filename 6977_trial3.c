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

int main(void){
    int n, numOne, numZero;

    scanf("%d %d", &n, &numOne);

    numZero = n-numOne;

    int leftZero = numZero;
    int leftOne = numOne;

    leftOne = 2;
    for(;leftZero>0;leftZero--){
        for(int i=0;i<=leftZero;i++){

            printf("1");
            leftOne --; // 1
            for(int j=0;j<numZero-leftZero+i;j++){
                printf("0");
            }

            printf("1");
            leftOne --; // 0
            for(int j=0;j<leftZero-i;j++){
                printf("0");
            }

            printf("\n");
        }
    }

    return 0;
}