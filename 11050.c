/*
문제
자연수 N과 정수 K가 주어졌을 때 이항 계수 (N,K)를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 0 ≤ K ≤ N)

출력 
(N,K)를 출력한다.
*/

#include <stdio.h>

int factorial(int n){
    int val = 1;
    for(int i=1;i<=n;i++){
        val *= i;
    }
    return val;
}

int permutation(int n, int k){
    int val = 1;
    for(int i=n;i>=n-k+1;i--){
        val *= i;
    }
    return val;
}

int main(){
    int N, K;
    scanf("%d %d", &N, &K);
    printf("%d", permutation(N, K)/factorial(K));
    return 0;
}