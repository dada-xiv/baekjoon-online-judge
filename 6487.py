'''
문제
두 개의 직선을 나타내는 4개의 점이 입력으로 주어질 때, 두 직선이 만나는지를 확인하는 프로그램을 작성하시오.

입력
입력의 첫 번째 줄에는 테스트 케이스의 개수 N이 주어진다. (N <= 10)

다음 N개의 줄에는 각각 8개의 정수 x1, y1, x2, y2, x3, y3, x4, y4가 주어진다. 이는 두 직선 (x1, y1)-(x2, y2)와 (x3, y3)-(x4, y4)를 나타낸다.

(x1, y1)과 (x2, y2)는 서로 다른 점이며, (x3, y3)와 (x4, y4)는 서로 다른 점임이 보장된다.

모든 x와 y는 [-1000, 1000] 범위 내의 정수이다.

출력
각각의 테스트 케이스에 대해, 다음과 같이 출력한다.

두 직선이 정확히 한 점에서 만난다면, POINT x y의 꼴로 출력한다. 이는 두 직선이 (x,y)에서 교차함을 의미한다. x와 y는 정확히 소숫점 아래 둘째 자리까지 출력한다.
두 직선이 만나지 않는다면, NONE을 출력한다.
두 직선이 무한히 많은 점에서 만난다면,  LINE을 출력한다.
'''

from sys import stdin
input = stdin.readline
n = int(input())
for _ in range(n):
  x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
  if (y1-y2)*(x3-x4) == (y3-y4)*(x1-x2):
    if x1 == x2 or x3 == x4:
      if ((x1 == x2 and x1 != x3) or (x3 == x4 and x3 != x1)):
        print("NONE")
      else:
        print("LINE")
    else:
      m1 = (y1 - y2)/(x1 - x2)
      m2 = (y3 - y4)/(x3 - x4)
      if (-m1*x1 + y1 != -m2*x3 + y3) or (x1-y1/m1 != x3-y3/m2):
        print("NONE")
      else:
        print("LINE")
  else:
    print("POINT", end=' ')
    if x1 == x2:
      m2 = (y3 - y4)/(x3 - x4)
      x = x1
      y = m2*(x1 - x3) + y3
    elif x3 == x4:
      m1 = (y1 - y2)/(x1 - x2)
      x = x3
      y = m1*(-x1 + x3) + y1
    else:
      m1 = (y1 - y2)/(x1 - x2)
      m2 = (y3 - y4)/(x3 - x4)
      x = (m1*x1 - m2*x3 - y1 + y3)/(m1 - m2)
      y = (-m2*y1 + m1*(m2*(x1 - x3) + y3))/(m1 - m2)
    print(format(x, ".2f"), format(y, ".2f"))
