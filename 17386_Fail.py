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

Ax, Ay, Bx, By = map(int, input().split())
Cx, Cy, Dx, Dy = map(int, input().split())
isCross = False

# 세 점이 일직선
# if (Ay - By)*(Cx - Dx) == (Cy - Dy)*(Ax - Bx):
#   isCross = False

if Ax == Bx:
  if Cx == Dx:
    isCross = False
  else:
    m2 = (Cy - Dy)/(Cx - Dx)
    x = Ax
    y = m2*(x - Cx) + Cy
    xmax = max(Cx, Dx)
    xmin = min(Cx, Dx)
    ymax = max(Cy, Dy)
    ymin = min(Cy, Dy)
    if (x <= xmax and x >= xmin) and (y <= ymax and y >= ymin):
      isCross = True
    else:
      isCross = False

if Cx == Dx:
  if Ax == Bx:
    isCross = False
  else:
    m1 = (Ay - By)/(Ax - Bx)
    x = Cx
    y = m1*(x - Ax) + Ay
    xmax = max(Ax, Bx)
    xmin = min(Ax, Bx)
    ymax = max(Ay, By)
    ymin = min(Ay, By)
    if (x <= xmax and x >= xmin) and (y <= ymax and y >= ymin):
      isCross = True
    else:
      isCross = False

if Ax != Bx and Cx != Dx:
  m1 = (Ay - By)/(Ax - Bx)
  m2 = (Cy - Dy)/(Cx - Dx)
  if m1 == m2:
    isCross = False
  else:
    x = (-Ay + Ax*m1 + Cy - Cx*m2)/(m1 - m2)
    y = m1*(x - Ax) + Ay
    # print(x,y)
    xmax = max(Ax, Bx)
    xmin = min(Ax, Bx)
    ymax = max(Ay, By)
    ymin = min(Ay, By)
    if (x <= xmax and x >= xmin) and (y <= ymax and y >= ymin):
      isCross = True
    else:
      isCross = False

if isCross:
  print(1)
else:
  print(0)
