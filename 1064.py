'''
문제
평행사변형은 평행한 두 변을 가진 사각형이다. 세 개의 서로 다른 점이 주어진다. A(xA,yA), B(xB,yB), C(xC,yC)

이때, 적절히 점 D를 찾아서 네 점으로 평행사변형을 만들면 된다. 이때, D가 여러 개 나올 수도 있다.

만들어진 모든 사각형 중 가장 큰 둘레 길이와 가장 작은 둘레 길이의 차이를 출력하는 프로그램을 작성하시오. 만약 만들 수 있는 평행사변형이 없다면 -1을 출력한다.

입력
첫째 줄에 xA yA xB yB xC yC가 주어진다. 모두 절댓값이 5000보다 작거나 같은 정수이다.

출력
첫째 줄에 문제의 정답을 출력한다. 절대/상대 오차는 10-9까지 허용한다.
'''


import math
Ax, Ay, Bx, By, Cx, Cy = map(int, input().split())
if (Ax == 0 and Bx == 0 and Cx == 0) or (Ay-By)*(Cx-Bx) == (Ax-Bx)*(Cy-By):
  print(-1)
else:
  a = math.sqrt((Bx-Cx)**2+(By-Cy)**2)
  b = math.sqrt((Ax-Cx)**2+(Ay-Cy)**2)
  c = math.sqrt((Bx-Ax)**2+(By-Ay)**2)
  maxL = max(a, b, c)
  minL = min(a, b, c)
  print(2*(maxL-minL))
