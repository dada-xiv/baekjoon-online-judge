'''
문제
2차원 좌표 평면 위의 두 선분 L1, L2가 주어졌을 때, 두 선분이 교차하는지 아닌지 구해보자.
L1의 양 끝 점은 (x1, y1), (x2, y2), L2의 양 끝 점은 (x3, y3), (x4, y4)이다.

입력
첫째 줄에 L1의 양 끝 점 x1, y1, x2, y2가, 둘째 줄에 L2의 양 끝 점 x3, y3, x4, y4가 주어진다. 세 점이 일직선 위에 있는 경우는 없다.

출력
L1과 L2가 교차하면 1, 아니면 0을 출력한다.

제한
-1,000,000 ≤ x1, y1, x2, y2, x3, y3, x4, y4 ≤ 1,000,000
x1, y1, x2, y2, x3, y3, x4, y4는 정수
선분의 길이는 0보다 크다.
'''


def ccw(Ax, Ay, Bx, By, Cx, Cy):
  ABx, ABy = Bx-Ax, By-Ay
  BCx, BCy = Cx-Bx, Cy-By
  val = ABx*BCy - ABy*BCx
  if val > 0:
    return 1
  elif val < 0:
    return -1
  else:
    return 0

Ax, Ay, Bx, By = map(int, input().split())
Cx, Cy, Dx, Dy = map(int, input().split())

if ccw(Ax, Ay, Bx, By, Cx, Cy)*ccw(Ax, Ay, Bx, By, Dx, Dy) == -1 and ccw(Cx, Cy, Dx, Dy, Ax, Ay)*ccw(Cx, Cy, Dx, Dy, Bx, By) == -1:
  print(1)
else:
  print(0)
