/*
문제
1을 한 번, 2를 두 번, 3을 세 번, 이런 식으로 1 2 2 3 3 3 4 4 4 4 5 .. 이러한 수열을 만들고 어느 일정한 구간을 주면 그 구간의 합을 구한다.

입력
첫째 줄에 구간의 시작과 끝을 나타내는 정수 A, B(1 ≤ A ≤ B ≤ 1,000)가 주어진다. 즉, 수열에서 A번째 숫자부터 B번째 숫자까지 합을 구하면 된다.

출력
첫 줄에 구간에 속하는 숫자의 합을 출력한다.
*/

#include <stdio.h>

int main(){
    int A, B;
    scanf("%d %d", &A, &B);
    int sum = 0;
    int cnt = 0;
    for(int i=1;cnt<=B;i++){
        for(int j=0;j<i;j++){
            cnt++;
            if(cnt>=A && cnt <=B){
                //printf("[%d] ", i);
                sum += i;
            }else if(cnt>B){
                break;
                //printf("%d ", i);
            }
        }
    }
    //printf("%\n");
    printf("%d", sum);
    return 0;
}