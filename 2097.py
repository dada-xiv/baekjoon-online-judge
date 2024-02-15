'''
문제
당신은 N개의 조약돌을 가지고 있다. 이 조약돌을 좌표평면의 격자점 위에 아무렇게나 떨어뜨렸다. 격자점이란, x좌표와 y좌표 모두가 정수인 지점을 말한다. 세 개의 조약돌을 (2,4), (4, 8), (5,5)에 떨어뜨렸다면, 이 세 조약돌을 모두 포함하는 가장 작은 직사각형은 가로 3, 세로 4인 직사각형이다. 이 경우 직사각형의 둘레는 14가 된다. 직사각형의 가로와 세로 길이는 반드시 1 이상이어야 한다.

조약돌의 개수 N이 주어졌을 때, 조약돌을 좌표평면의 격자점에 적절히 떨어뜨려서 모든 조약돌을 포함하는 직사각형의 둘레를 최소로 하는 프로그램을 작성하시오.

입력
첫째 줄에 조약돌의 개수 N(1 ≤ n ≤ 500,000,000)이 주어진다.

출력
첫째 줄에 최소 둘레를 출력한다.
'''

import math
n = int(input())
sqN = math.sqrt(n)
rsqN = round(sqN)
# print(f"{n}:{rsqN}", end=' ')
# print(sqN < rsqN, end=' ')
if n <= 2:
  surroundings = 4
elif sqN.is_integer():
  surroundings = int((sqN-1)*4)
elif sqN < rsqN:
  surroundings = (rsqN-1)*4
else:
  surroundings = (rsqN-1)*4+2
print(surroundings)
