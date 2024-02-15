/*
문제
이동통신사는 다음 두 가지 요금제 중 하나를 선택하라고 했다.

- Y요금제는 30초마다 10원씩 청구된다. 만약 29초 또는 그 보다 적게 통화를 하면 10원이 청구된다. 만약 30초에서 59초 사이의 시간 동안 통화를 한다면 20원이 청구된다.

- M요금제는 60초마다 15원씩 청구된다. 만약 59초 또는 그 보다 적게 통화를 하면 15원이 청구된다. 만약 60초에서 119초 사이의 시간 동안 통화를 한다면 30원이 청구된다.

한 달 동인 이용한 통화 내역이 주어지면 어느 요금제를 사용하는 것이 저렴한지 출력하는 프로그램을 작성하시오.

입력
첫째 줄에는 지난 달에 이용한 통화 내역의 총 갯수 N개가 주어진다. N은 20보다 작거나 같은 자연수이다. 둘째 줄에는 N개 내역 각각의 통화 시간이 초 단위로 주어진다. 통화 시간은 10,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 Y와 M 둘 중에서 싼 요금제를 출력한다. 그 후에 공백을 사이에 두고 요금이 몇 원 나오는지 출력한다. 만약 두 요금제의 요금이 모두 같다면 Y를 출력한다.

예제 입력 1 
3
40 40 40

예제 출력 1 
M 45
*/

#include <stdio.h>

int main(){
    int N;
    int val;
    int ySum = 0;
    int mSum = 0;

    scanf("%d", &N);

    for(int i=0;i<N;i++){
        scanf("%d", &val);
        ySum += (val/30+1)*10;
        mSum += (val/60+1)*15;
    }

    if(ySum < mSum){
        printf("Y %d",ySum);
    }else if(ySum > mSum){
        printf("M %d",mSum);
    }else{
        printf("Y M %d",ySum);
    }

    return 0;
}