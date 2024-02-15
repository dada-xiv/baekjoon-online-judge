'''
문제
2차원 평면에 N개의 점이 주어져 있다. 이 중에서 세 점을 골랐을 때, 직각삼각형이 몇 개나 있는지를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 점의 개수 N(3 ≤ N ≤ 1,500)이 주어진다. 둘째 줄부터 N개의 줄에 걸쳐 각 점의 x좌표와 y좌표가 빈 칸을 사이에 두고 주어진다. 좌표값은 절댓값이 1,000,000,000을 넘지 않는 정수이며, 주어지는 모든 점의 좌표는 다르다.

출력
첫째 줄에 직각삼각형의 개수를 출력한다.
'''

from sys import stdin
input = stdin.readline

def gcd(m, n):
  while n:
    m, n = n, m % n
  return m

n = int(input())
pt = []
for _ in range(n):
  x, y = map(int, input().split())
  pt.append((x, y))

cnt = 0
for i in range(n):
  multi = {}
  for j in range(n):
    if i == j:
      continue
    x = pt[i][0]-pt[j][0]
    y = pt[i][1]-pt[j][1]
    g = gcd(x, y)
    if g < 0:
      g = -g
    x = x//g
    y = y//g
    multi[(x, y)] = multi.get((x, y), 0)+1

  for mX, mY in multi:
    if (mY, -mX) in multi:
      cnt += multi[(mX, mY)]*multi[(mY, -mX)]

print(cnt)
