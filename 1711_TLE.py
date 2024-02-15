'''
문제
2차원 평면에 N개의 점이 주어져 있다. 이 중에서 세 점을 골랐을 때, 직각삼각형이 몇 개나 있는지를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 점의 개수 N(3 ≤ N ≤ 1,500)이 주어진다. 둘째 줄부터 N개의 줄에 걸쳐 각 점의 x좌표와 y좌표가 빈 칸을 사이에 두고 주어진다. 좌표값은 절댓값이 1,000,000,000을 넘지 않는 정수이며, 주어지는 모든 점의 좌표는 다르다.

출력
첫째 줄에 직각삼각형의 개수를 출력한다.
'''

from itertools import combinations
from sys import stdin
input = stdin.readline

def isRtriangle(A, B, C):
  Ax, Ay = A[0], A[1]
  Bx, By = B[0], B[1]
  Cx, Cy = C[0], C[1]
  AB2 = (Ax-Bx)**2+(Ay-By)**2
  BC2 = (Cx-Bx)**2+(Cy-By)**2
  CA2 = (Ax-Cx)**2+(Ay-Cy)**2
  if AB2+BC2 == CA2 or AB2+CA2 == BC2 or CA2+BC2 == AB2:
    return True
  else:
    return False

n = int(input())
pt = []
for _ in range(n):
  x, y = map(int, input().split())
  pt.append((x, y))

cnt = 0
for ele in combinations(pt, 3):
  if isRtriangle(ele[0], ele[1], ele[2]):
    cnt += 1
print(cnt)
