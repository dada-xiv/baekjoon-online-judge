'''
문제
마인크래프트는 1 × 1 × 1(세로, 가로, 높이) 크기의 블록들로 이루어진 세계에서 땅을 파거나 집을 지을 수 있는 게임이다. 고르지 않은 땅에는 집을 지을 수 없기 때문에 땅의 높이를 모두 동일하게 만드는 땅 고르기 작업을 해야 한다.

세로 N, 가로 M 크기의 집터가 주어지며 맨 왼쪽 위의 좌표는 (0, 0)이다. 목적은 이 집터 내의 땅의 높이를 일정하게 바꾸는 것이다. 다음과 같은 두 종류의 작업을 할 수 있다:
1. 좌표 (i, j)의 가장 위에 있는 블록을 제거하여 인벤토리에 넣는다.
2. 인벤토리에서 블록 하나를 꺼내어 좌표 (i, j)의 가장 위에 있는 블록 위에 놓는다.

1번 작업은 2초가 걸리며, 2번 작업은 1초가 걸린다. 땅 고르기 작업에 걸리는 최소 시간과 작업 후 땅의 높이를 출력하시오.

빈 공간은 존재하지 않으며, 바깥에서 블록을 가져올 수 없다. 시작할 때 인벤토리에는 B개의 블록이 들어 있다. 땅의 높이는 256블록을 초과할 수 없으며, 음수가 될 수 없다.

입력
첫째 줄에 N, M, B가 주어진다. (1 ≤ M, N ≤ 500, 0 ≤ B ≤ 6.4 × 10^7)

둘째 줄부터 N개의 줄에 각각 M개의 정수로 땅의 높이가 주어진다. (i + 2)번째 줄의 (j + 1)번째 수는 좌표 (i, j)에서의 땅의 높이를 나타낸다. 땅의 높이는 256보다 작거나 같은 자연수 또는 0이다.

출력
첫째 줄에 땅을 고르는 데 걸리는 시간과 땅의 높이를 출력하시오. 답이 여러 개 있다면 그중에서 땅의 높이가 가장 높은 것을 출력하시오.
'''

from sys import stdin
input = stdin.readline

n, m, b = map(int, input().split())
g = list()
for _ in range(n):
  tmp = list(map(int, input().split()))
  g += tmp

g.sort()
gsum = sum(g)

th = g[0]  # target height
thMax = g[n*m-1]

res = list()
while True:
  invB = b
  timeD = 0
  for bnum in g:
    if bnum >= th:
      timeD += (bnum-th)*2
      invB += bnum-th
    else:
      timeD += th-bnum
      invB -= th-bnum
      pass
  if invB<0:
    break
  else:
    res.append([timeD, th])
    th += 1

res = sorted(res, key=lambda x: (x[0], -x[1]))
print(res[0][0], res[0][1])
