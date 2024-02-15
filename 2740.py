'''
문제
N*M크기의 행렬 A와 M*K크기의 행렬 B가 주어졌을 때, 두 행렬을 곱하는 프로그램을 작성하시오.

입력
첫째 줄에 행렬 A의 크기 N 과 M이 주어진다. 둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 순서대로 주어진다. 그 다음 줄에는 행렬 B의 크기 M과 K가 주어진다. 이어서 M개의 줄에 행렬 B의 원소 K개가 차례대로 주어진다. N과 M, 그리고 K는 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.

출력
첫째 줄부터 N개의 줄에 행렬 A와 B를 곱한 행렬을 출력한다. 행렬의 각 원소는 공백으로 구분한다.
'''

from sys import stdin
input = stdin.readline

a = list()
b = list()

N, M = map(int, input().split())
for _ in range(N):
  a.append(list(map(int, input().split())))
M, K = map(int, input().split())
for _ in range(M):
  b.append(list(map(int, input().split())))

c = list()
for _ in range(N):
  c.append([0 for i in range(K)])

for i in range(N):
  for j in range(K):
    sum = 0
    for k in range(M):
      sum += a[i][k]*b[k][j]
      c[i][j] = sum

for row in c:
  print(' '.join(map(str, row)))
