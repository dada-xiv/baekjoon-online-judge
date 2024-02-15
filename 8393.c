/*
입력
첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.

출력
1부터 n까지 합을 출력한다.
 */

#include <stdio.h>

int main(void){
    int n, sum=0;

    scanf("%d", &n);

    for(int i=1;i<=n;i++){
        sum += i;
    }

    printf("%d", sum);
    
    return 0;
}