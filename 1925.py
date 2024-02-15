'''
문제
평면상에 세 개의 점이 주어지면, 그 세 점으로 이루어지는 삼각형은 유일하게 결정된다. 또는, 삼각형이 이루어지지 않기도 한다. 세 점의 좌표가 주어졌을 때 다음에 따라 이 삼각형의 종류를 판단하는 프로그램을 작성하시오.

1. 세 점이 일직선 위에 있으면 - ‘삼각형이 아님’  출력할 때는 X

2. 세 변의 길이가 같으면 - ‘정삼각형’ 출력할 때는 JungTriangle

3. 두 변의 길이가 같으면
가장 큰 각이 90°보다 크면 - ‘둔각이등변삼각형’ 출력할 때는 Dunkak2Triangle
가장 큰 각이 90°이면 - ‘직각이등변삼각형’ 출력할 때는 Jikkak2Triangle
가장 큰 각이 90°보다 작으면 - ‘예각이등변삼각형’ 출력할 때는 Yeahkak2Triangle

4. 세 변의 길이가 모두 다르면
가장 큰 각이 90°보다 크면 - ‘둔각삼각형’ 출혁할 때는 DunkakTriangle
가장 큰 각이 90°이면 - ‘직각삼각형’ 출력할 때는 JikkakTriangle
가장 큰 각이 90°보다 작으면 - ‘예각삼각형’ 출력할 때는 YeahkakTriangle

입력
첫째 줄부터 셋째 줄까지 삼각형을 이루는 점의 x좌표와 y좌표가 빈칸을 사이에 두고 주어진다. 입력되는 수는 절댓값이 10,000을 넘지 않는 정수이다. 입력으로 주어지는 세 좌표는 중복되지 않는다.

출력
위의 경우에 따라 삼각형의 종류가 무엇인지 출력한다.
'''

def getMax(a, b, c):
  if a > b:
    return 1 if a > c else 3
  else:
    return 2 if b > c else 3

def kak(a2, b2, c2):
  if a2+b2 == c2:
    return "Jikkak"
  elif a2+b2 < c2:
    return "Dunkak"
  else:
    return "Yeahkak"

Ax, Ay = map(int, input().split())
Bx, By = map(int, input().split())
Cx, Cy = map(int, input().split())

if (By-Ay)*(Cx-Bx) == (Bx-Ax)*(Cy-By):
  print("X")
else:
  a2 = (Bx-Cx)**2+(By-Cy)**2
  b2 = (Ax-Cx)**2+(Ay-Cy)**2
  c2 = (Ax-Bx)**2+(Ay-By)**2
  if a2 == b2 or b2 == c2 or c2 == a2:
    if a2 == b2 and b2 == c2 and c2 == a2:
      print("JungTriangle")
    else:
      if a2 == b2:
        print(kak(a2, b2, c2)+"2Triangle")
      elif b2 == c2:
        print(kak(b2, c2, a2)+"2Triangle")
      elif c2 == a2:
        print(kak(c2, a2, b2)+"2Triangle")
  else:
    if getMax(a2,b2,c2)==1:
      print(kak(b2, c2, a2)+"Triangle")
    elif getMax(a2,b2,c2)==2:
      print(kak(c2, a2, b2)+"Triangle")
    else:
      print(kak(a2, b2, c2)+"Triangle")

