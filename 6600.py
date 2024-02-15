'''
문제
일직선 상에 있지 않은 세 점이 주어진다. 이 세 점을 이용해서 만들 수 있는 원의 원주를 구하는 프로그램을 작성하시오.

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스는 한 줄로 이루어져 있고, 실수 x1, y1, x2, y2, x3, y3이 주어진다. 세 점으로 만들 수 있는 원의 지름은 백만을 넘지 않는다.

출력
각 테스트 케이스마다 입력으로 주어진 원의 원주를 소수점 둘째 짜리까지 반올림해 출력한다. 파이의 근사값은 3.141592653589793이다.
'''


import math
import sys
input = sys.stdin.readline

def roundT(val, digits):
  return round(val+10**(-len(str(val))-1), digits)

PI = 3.141592653589793

for s in sys.stdin:
  Ax, Ay, Bx, By, Cx, Cy = map(float, s.split())
  # Ax, Ay, Bx, By, Cx, Cy = map(float, input().split())
  d1x, d1y = (Ax + Bx)/2, (Ay + By)/2
  d2x, d2y = (Bx + Cx)/2, (By + Cy)/2
  d3x, d3y = (Cx + Ax)/2, (Cy + Ay)/2
  if Ay != By and By!=Cy:
    m1 = -(Ax - Bx)/(Ay - By)
    m2 = -(Bx - Cx)/(By - Cy)
    x = (-d1y + d2y + d1x*m1 - d2x*m2)/(m1 - m2)
    y = m1*(x - d1x) + d1y
  elif By!=Cy and Cy!=Ay:
    m2 = -(Bx - Cx)/(By - Cy)
    m3 = -(Cx - Ax)/(Cy - Ay)
    x = (-d2y + d3y + d2x*m2 - d3x*m3)/(m2 - m3)
    y = m2*(x - d2x) + d2y
  elif Ay!=By and Cy!=Ay:
    m1 = -(Ax - Bx)/(Ay - By)
    m3 = -(Cx - Ax)/(Cy - Ay)
    x = (-d1y + d3y + d1x*m1 - d3x*m3)/(m1 - m3)
    y = m1*(x - d1x) + d1y
  r = math.sqrt((x-Ax)**2+(y-Ay)**2)
  print(roundT(2*PI*r, 2))
