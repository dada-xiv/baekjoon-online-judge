'''
문제
파이프에서 물이 새는 곳은 가장 왼쪽에서 정수만큼 떨어진 거리만 물이 샌다. 길이가 L인 테이프를 무한개 가지고 있다. 물을 막을 때, 적어도 그 위치의 좌우 0.5만큼 간격을 줘야 물이 안 샌다.

물이 새는 곳의 위치와, 가지고 있는 테이프의 길이 L이 주어졌을 때, 필요한 테이프의 최소 개수를 구하는 프로그램을 작성하시오. 테이프를 자를 수 없고, 테이프를 겹쳐서 붙이는 것도 가능하다.

입력
첫째 줄에 물이 새는 곳의 개수 N과 테이프의 길이 L이 주어진다. 둘째 줄에는 물이 새는 곳의 위치가 주어진다. N과 L은 1,000보다 작거나 같은 자연수이고, 물이 새는 곳의 위치는 1,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 필요한 테이프의 개수를 출력한다.
'''

from sys import stdin
input = stdin.readline
N, L = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
tStart = 0
tStart = a[0]
tEnd = a[0]
cnt = 1
for i in range(1, N):
  if a[i]-tStart < L:
    tEnd = a[i]
  else:
    cnt += 1
    tStart = a[i]
    tEnd = a[i]

print(cnt)
