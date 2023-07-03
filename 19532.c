/*
문제
다음 연립방정식에서 $x$와 $y$의 값을 계산하시오.
 
\[\begin{cases}ax+by=c\\dx+ey=f\end{cases}\] 
각 칸에는 $-999$ 이상 $999$ 이하의 정수만 입력할 수 있다.

입력
정수 $a$, $b$, $c$, $d$, $e$, $f$가 공백으로 구분되어 차례대로 주어진다. ($-999 \leq a,b,c,d,e,f \leq 999$)

문제에서 언급한 방정식을 만족하는 $\left(x,y\right)$가 유일하게 존재하고, 이 때 $x$와 $y$가 각각 $-999$ 이상 $999$ 이하의 정수인 경우만 입력으로 주어짐이 보장된다.

출력
문제의 답인 $x$와 $y$를 공백으로 구분해 출력한다.
 */

#include <stdio.h>

int main(void){
    int a, b, c, d, e, f;
    int x, y;

    scanf("%d %d %d %d %d %d", &a, &b, &c, &d, &e, &f);

    x = -(c*e - b*f)/(b*d - a*e);
    y = -(-c*d + a*f)/(b*d - a*e);

    printf("%d %d", x, y);

    return 0;
}