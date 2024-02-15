/*
문제
[1]부터 [34]까지의 카드가 무한히 많다. 숫자가 순서대로 주어질 때, 가능한 카드의 배열이 모두 몇 개인지 구하는 프로그램을 작성하시오. 예를들어 27123은 여섯 가지 경우가 있다
[27][1][2][3]
[27][12][3]
[27][1][23]
[2][7][1][2][3]
[2][7][12][3]
[2][7][1][23]

입력
첫 줄에 숫자가 순서대로 주어지며, 이것은 최대 40자 이하의 숫자로 이루어진다.

출력
첫 줄에 가능한 카드 배열이 몇 개인지를 출력한다.
*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define SIZE 41

int cntWays(char s[]) {
    int n = strlen(s);
    int dp[n+1];
    memset(dp, 0, sizeof(dp));
    dp[0] = 1;

    for (int i=1;i<=n;i++) {
        for (int j=1; j<=3 && j<=i;j++) {
            char sub[j+1];
            strncpy(sub, s+(i-j), j);
            sub[j] = '\0';
            if (sub[0]!='0' && atoi(sub)<=34) {
                dp[i] += dp[i-j];
            }
        }
    }

    return dp[n];
}

int main() {
    char a[SIZE];
    scanf("%s", a);
    printf("%d\n", cntWays(a));
    return 0;
}
