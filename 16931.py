'''
문제
크기가 N×M인 종이가 있고, 종이는 1×1크기의 칸으로 나누어져 있다. 이 종이의 각 칸 위에 1×1×1 크기의 정육면체를 놓아 3차원 도형을 만들었다.

종이의 각 칸에 놓인 정육면체의 개수가 주어졌을 때, 이 도형의 겉넓이를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 종이의 크기 N, M이 주어진다. 둘째 줄부터 N개의 줄에는 종이의 각 칸에 놓인 정육면체의 수가 주어진다.

출력
첫째 줄에 도형의 겉넓이를 출력한다.

제한
1 ≤ N, M ≤ 100
1 ≤ 종이의 한 칸에 놓인 정육면체의 수 ≤ 100
'''

from sys import stdin
input = stdin.readline
n, m = map(int, input().split())

a = list()
for _ in range(n):
  a.append(list(map(int, input().split())))

sum = 0

for i in range(n):
  sumv = 0
  preh = 0
  for j in range(m):
    diff = a[i][j]-preh
    if diff > 0:
      sumv += diff
    preh = a[i][j]
  sum += sumv

for i in range(n):
  sumv = 0
  preh = 0
  for j in range(m-1, -1, -1):
    diff = a[i][j]-preh
    if diff > 0:
      sumv += diff
    preh = a[i][j]
  sum += sumv

for j in range(m):
  sumv = 0
  preh = 0
  for i in range(n):
    diff = a[i][j]-preh
    if diff > 0:
      sumv += diff
    preh = a[i][j]
  sum += sumv

for j in range(m):
  sumv = 0
  preh = 0
  for i in range(n-1, -1, -1):
    diff = a[i][j]-preh
    if diff > 0:
      sumv += diff
    preh = a[i][j]
  sum += sumv

print(sum+2*(n*m))
