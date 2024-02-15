'''
문제
네 점이 주어졌을 때, 네 점을 이용해 정사각형을 만들 수 있는지 없는지를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 네 줄로 이루어져 있으며, 점의 좌표가 한 줄에 하나씩 주어진다. 점의 좌표는 -100,000보다 크거나 같고, 100,000보다 작거나 같은 정수이다. 같은 점이 두 번 이상 주어지지 않는다.

출력
각 테스트 케이스마다 입력으로 주어진 네 점을 이용해서 정사각형을 만들 수 있으면 1을, 없으면 0을 출력한다.
'''

from sys import stdin
input = stdin.readline
T = int(input())
for _ in range(T):
  Ax, Ay = map(int, input().split())
  Bx, By = map(int, input().split())
  Cx, Cy = map(int, input().split())
  Dx, Dy = map(int, input().split())
  A = (Ax, Ay)
  B = (Bx, By)
  C = (Cx, Cy)
  D = (Dx, Dy)
  C1 = (Ax - Ay + By, Ax + Ay - Bx)
  D1 = (-Ay + Bx + By, Ax - Bx + By)
  C2 = (Ax + Ay - By, -Ax + Ay + Bx)
  D2 = (Ay + Bx - By, -Ax + Bx + By)
  C3 = (int((Ax + Ay + Bx - By)/2), int((-Ax + Ay + Bx + By)/2))
  D3 = (int((Ax - Ay + Bx + By)/2), int((Ax + Ay - Bx + By)/2))
  setIn = {A, B, C, D}
  set1 = {A, B, C1, D1}
  set2 = {A, B, C2, D2}
  set3 = {A, B, C3, D3}
  if setIn == set1 or setIn == set2 or setIn == set3:
    print(1)
  else:
    print(0)
