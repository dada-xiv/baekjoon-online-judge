'''
문제
크기가 N×M인 행렬 A와 M×K인 B를 곱할 때 필요한 곱셈 연산의 수는 총 N×M×K번이다. 행렬 N개를 곱하는데 필요한 곱셈 연산의 수는 행렬을 곱하는 순서에 따라 달라지게 된다.

예를 들어, A의 크기가 5×3이고, B의 크기가 3×2, C의 크기가 2×6인 경우에 행렬의 곱 ABC를 구하는 경우

- AB를 먼저 곱하고 C를 곱하면 (AB)C에 필요한 곱셈 연산의 수는 5×3×2 + 5×2×6 = 30 + 60 = 90번
- BC를 먼저 곱하고 A를 곱하면 A(BC)에 필요한 곱셈 연산의 수는 5×3×6 + 3×2×6 = 90 + 36 = 126번

행렬 N개의 크기가 주어졌을 때, 모든 행렬을 곱하는데 필요한 곱셈 연산 횟수의 최솟값을 구하는 프로그램을 작성하시오. 입력으로 주어진 행렬의 순서를 바꾸면 안 된다.

입력
첫째 줄에 행렬의 개수 N(1 ≤ N ≤ 500)이 주어진다.
둘째 줄부터 N개 줄에는 행렬의 크기 r과 c가 주어진다. (1 ≤ r, c ≤ 500)
항상 순서대로 곱셈을 할 수 있는 크기만 입력으로 주어진다.

출력
첫째 줄에 입력으로 주어진 행렬을 곱하는데 필요한 곱셈 연산의 최솟값을 출력한다. 정답은 2^{31}-1 보다 작거나 같은 자연수이다. 또한, 최악의 순서로 연산해도 연산 횟수가 2^{31}-1보다 작거나 같다.
'''

'''
아래 코드는 다음을 처리하지 못한다:

5
1 10
10 1
1 10
10 1
1 10
(31)

구체적으로

(1, 1) (1, 10) 10
(1, 10) (10, 1) 10

에서 뒤의 것을 먼저 빼내지 못한다
'''

# from collections import deque
from sys import stdin
input = stdin.readline
N = int(input())
q = list()
for _ in range(N):
  a, b = map(int, input().split())
  q.append((a, b))

print(q)


sum = 0

for _ in range(N-1):
  min = 500**3
  minidx = -1
  for i in range(len(q)-1):
    print(q[i], q[i+1], end=' ')
    val = q[i][0]*q[i][1]*q[i+1][1]
    print(val)
    if val < min:
      min = val
      minidx = i

  sum += min
  print(min, minidx)
  q.insert(minidx, (q[minidx][0], q[minidx+1][1]))
  # print(q)
  del q[minidx+1]
  del q[minidx+1]
  print(q)

print(sum)