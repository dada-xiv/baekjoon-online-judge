'''
문제
가로, 세로의 크기가 각각 100인 정사각형 모양의 흰색 도화지가 있다. 이 도화지 위에 가로, 세로의 크기가 각각 10인 정사각형 모양의 검은색 색종이를 색종이의 변과 도화지의 변이 평행하도록 붙인다. 이러한 방식으로 색종이를 한 장 또는 여러 장 붙인 후 색종이가 붙은 검은 영역의 둘레의 길이를 구하는 프로그램을 작성하시오.

예를 들어 흰색 도화지 위에 네 장의 검은색 색종이를 <그림 1>과 같은 모양으로 붙였다면 검은색 영역의 둘레는 96 이 된다.

<그림 1>

입력
첫째 줄에 색종이의 수가 주어진다. 이어 둘째 줄부터 한 줄에 하나씩 색종이를 붙인 위치가 주어진다. 색종이를 붙인 위치는 두 개의 자연수로 주어지는데 첫 번째 자연수는 색종이의 왼쪽 변과 도화지의 왼쪽 변 사이의 거리이고, 두 번째 자연수는 색종이의 아래쪽 변과 도화지의 아래쪽 변 사이의 거리이다. 색종이의 수는 100이하이며, 색종이가 도화지 밖으로 나가는 경우는 없다. 

출력
첫째 줄에 색종이가 붙은 검은 영역의 둘레의 길이를 출력한다.
'''

from sys import stdin
input = stdin.readline

L = 100
a = [[0 for _ in range(L)] for _ in range(L)]

def putpaper(x, y):
  for i in range(L):
    for j in range(L):
      if (i >= x and i < x+10) and (j >= y and j < y+10):
        a[i][j] = 1

n = int(input())
for _ in range(n):
  x, y = map(int, input().split())
  putpaper(x, y)

# for i in range(L):
#   for j in range(L):
#     print(a[i][j], end='')
#   print()

length = 0
for i in range(L):
  for j in range(L):
    if (j == 0 or j == L-1) and a[i][j] == 1:
      length += 1
    if j > 0 and (a[i][j-1] == 0 and a[i][j] == 1):
      length += 1
    if j < L-1 and (a[i][j] == 1 and a[i][j+1] == 0):
      length += 1

for j in range(L):
  for i in range(L):
    if (i == 0 or i == L-1) and a[i][j] == 1:
      length += 1
    if i > 0 and (a[i-1][j] == 0 and a[i][j] == 1):
      length += 1
    if i < L-1 and (a[i][j] == 1 and a[i+1][j] == 0):
      length += 1

print(length)
