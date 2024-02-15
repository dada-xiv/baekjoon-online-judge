'''
문제
A와 B에게 C의 위치를 계산하라는 명령을 내렸다. A와 B는 각각 자신의 위치에서 C까지의 거리를 계산했다.

 A의 좌표 $(x_1, y_1)$와 B의 좌표 $(x_2, y_2)$가 주어지고, A가 계산한 C와의 거리 $r_1$과 B가 계산한 C와의 거리 $r_2$가 주어졌을 때, C가 있을 수 있는 좌표의 수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 $T$가 주어진다. 각 테스트 케이스는 다음과 같이 이루어져 있다.

한 줄에 공백으로 구분 된 여섯 정수 $x_1$, $y_1$, $r_1$, $x_2$, $y_2$, $r_2$가 주어진다.

출력
각 테스트 케이스마다 C가 있을 수 있는 위치의 수를 출력한다. 만약 C가 있을 수 있는 위치의 개수가 무한대일 경우에는 -1을 출력한다.

제한
-10000 ≤ x_1, y_1, x_2, y_2 ≤ 10000
1 ≤ r_1, r_2 ≤ 10000
'''

import math

def getMax(a, b, c):
    if a > b:
        return a if a > c else c
    else:
        return b if b > c else c

def numTriangle(a, b, c): 
    sum = a+b+c
    max = getMax(a, b, c)
    sumR = sum - max
    n = 2
    if sumR < max:
        n = 0
    elif sumR == max:
        n = 1
    return n

def isEqual(x1, y1, x2, y2):
    if(x1==x2 and y1==y2):
        return True
    else:
        return False

T = int(input())

d = 0
r = 0
res = 0

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = math.sqrt((x1-x2)**2+(y1-y2)**2)
    r = r1 + r2

    if isEqual(x1, y1, x2, y2):
        if r == 0:
            res = 1
        else:
            if r1==r2:
                res = -1
            else:
                res = 0
    else:
        if r1+r2 < d:
            res = 0
        elif r1+r2 == d:
            res = 1
        else:
            res = numTriangle(r1, r2, d)

    print(res)