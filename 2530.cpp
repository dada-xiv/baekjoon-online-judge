/*
문제
요리를 시작하는 시각과 오븐구이를 하는 데 필요한 시간이 초 단위로 주어졌을 때, 오븐구이가 끝나는 시각을 계산하는 프로그램을 작성하시오.

입력
첫째 줄에는 현재 시각이 나온다. 현재 시각은 시 A (0 ≤ A ≤ 23), 분 B (0 ≤ B ≤ 59)와 초 C (0 ≤ C ≤ 59)가 정수로 빈칸을 사이에 두고 순서대로 주어진다. 두 번째 줄에는 요리하는 데 필요한 시간 D (0 ≤ D ≤ 500,000)가 초 단위로 주어진다.

출력
첫째 줄에 종료되는 시각의 시, 분, 초을 공백을 사이에 두고 출력한다. (단, 시는 0부터 23까지의 정수이며, 분, 초는 0부터 59까지의 정수이다. 디지털 시계는 23시 59분 59초에서 1초가 지나면 0시 0분 0초가 된다.)
*/

#include <iostream>
using namespace std;
int main(){
    int hour, min, sec;
    int cookSec;

    cin >> hour >> min >> sec;
    cin >> cookSec; // seconds

    int cHour = cookSec / 3600;
    int cMin = (cookSec-cHour*3600) / 60;
    int cSec = (cookSec-cMin*60) % 60;

    int fHour = hour + cHour;
    int fMin = min + cMin;
    int fSec = sec + cSec;

    if(fSec >= 60){
        fMin += fSec/60;
        fSec = fSec%60;
    }

    if(fMin >= 60){
        fHour += fMin/60;
        fMin = fMin%60;
    }

    if(fHour >= 24){
        fHour = fHour%24;
    }

    printf("%d %d %d", fHour, fMin, fSec);

    return 0;
}