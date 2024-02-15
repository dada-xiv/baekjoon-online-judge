'''
문제
우주선은 행성계 간의 이동을 최대한 피해서 여행해야 한다. 원은 행성계의 경계를 의미한다. 출발점, 도착점이 주어졌을 때 필요한 최소의 행성계 진입/이탈 횟수를 구하는 프로그램을 작성해 보자. 행성계의 경계가 맞닿거나 서로 교차하는 경우는 없다. 또한, 출발점이나 도착점이 행성계 경계에 걸쳐진 경우 역시 입력으로 주어지지 않는다.

입력
입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 그 다음 줄부터 각각의 테스트케이스에 대해 첫째 줄에 출발점 (x1, y1)과 도착점 (x2, y2)이 주어진다. 두 번째 줄에는 행성계의 개수 n이 주어지며, 세 번째 줄부터 n줄에 걸쳐 행성계의 중점과 반지름 (cx, cy, r)이 주어진다.

출력
각 테스트 케이스에 대해 거쳐야 할 최소의 행성계 진입/이탈 횟수를 출력한다.
'''

from sys import stdin
input = stdin.readline

def isinC(cx, cy, cr, x, y):
  if (cx-x)**2+(cy-y)**2 < cr**2:
    return 1
  else:
    return 0

t = int(input())
for _ in range(t):
  x1, y1, x2, y2 = map(int, input().split())
  n = int(input())
  cnt = 0
  for _ in range(n):
    cx, cy, cr = map(int, input().split())
    if isinC(cx, cy, cr, x1, y1)+isinC(cx, cy, cr, x2, y2) == 1:
      cnt += 1
  print(cnt)
