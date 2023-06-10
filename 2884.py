'''
원래 설정되어 있는 알람을 45분 앞서는 시간으로 바꾸기 

입력
첫째 줄에 두 정수 H와 M이 주어진다. (0 ≤ H ≤ 23, 0 ≤ M ≤ 59) 그리고 이것은 현재 설정한 알람 시간 H시 M분을 의미한다.

입력 시간은 24시간 표현을 사용한다. 24시간 표현에서 하루의 시작은 0:0(자정)이고, 끝은 23:59(다음날 자정 1분 전)이다. 시간을 나타낼 때, 불필요한 0은 사용하지 않는다.

출력
첫째 줄에 설정해야 하는 알람 시간을 출력한다. (입력과 같은 형태로 출력하면 된다.)
'''

def getAlamTime(inHour, inMin):
    outHour = inHour
    outMin = inMin - 45

    #6시 -2분은 5시 58분과 같다.
    if outMin < 0 :
        outMin += 60
        outHour -= 1
    #-2시 23분은 22시 23분과 같다.
    if outHour < 0 :
        outHour += 24
    
    return outHour, outMin

H, M = map(int, input().split())

print(
    " ".join(map(str, getAlamTime(H, M)))
)
