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

#define SIZE 31

int main(void){
    int n, k;
    long long int num = 0;
    char a[SIZE];
    int i;
    int j;

    scanf("%d %d", &n, &k);
/*
    for(int i=n-1;i>=n-k;i--){
        num += pow(2,i);
    }
    printf("%lld", num);
*/

    for(j=0;j<=n-k;j++){
        i = 0;

        a[i] = '1';
        for(i=1;i<=(0+j);i++){
            a[i] = '0';
        }

        for(;i<(k+j);i++){
            a[i] = '1';
        }
        for(;i<n;i++){
            a[i] = '0';
        }
        
        a[i+1] += '\0';
        printf("%s\n", a);
    }

    return 0;
}