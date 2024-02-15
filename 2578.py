'''
문제
빙고 게임은 다음과 같은 방식으로 이루어진다. 먼저 25개의 칸으로 이루어진 빙고판에 1부터 25까지 자연수를 한 칸에 하나씩 쓴다. 다음은 사회자가 부르는 수를 차례로 지워나간다. 차례로 수를 지워가다가 같은 가로줄, 세로줄 또는 대각선 위에 있는 5개의 모든 수가 지워지는 경우 그 줄에 선을 긋는다. 이러한 선이 세 개 이상 그어지는 순간 "빙고"라고 외치는데, 가장 먼저 외치는 사람이 게임의 승자가 된다. 철수가 빙고판에 쓴 수들과 사회자가 부르는 수의 순서가 주어질 때, 사회자가 몇 번째 수를 부른 후 철수가 "빙고"를 외치게 되는지를 출력하는 프로그램을 작성하시오.

입력
첫째 줄부터 다섯째 줄까지 빙고판에 쓰여진 수가 가장 위 가로줄부터 차례대로 한 줄에 다섯 개씩 빈 칸을 사이에 두고 주어진다. 여섯째 줄부터 열째 줄까지 사회자가 부르는 수가 차례대로 한 줄에 다섯 개씩 빈 칸을 사이에 두고 주어진다. 빙고판에 쓰여진 수와 사회자가 부르는 수는 각각 1부터 25까지의 수가 한 번씩 사용된다.

출력
첫째 줄에 사회자가 몇 번째 수를 부른 후 철수가 "빙고"를 외치게 되는지 출력한다.
'''

from sys import stdin
input = stdin.readline

def checkBingo(a):
  res = 0
  for row in a:
    if row.count(0) == 5:
      res += 1

  for j in range(5):
    cntCol = 0
    for i in range(5):
      if a[i][j] == 0:
        cntCol += 1
    if cntCol == 5:
      res += 1

  cntColD1 = 0  # 00 11 22 33 44
  for i in range(5):
    if a[i][i] == 0:
      cntColD1 += 1
  if cntColD1 == 5:
    res += 1

  cntColD2 = 0  # 04 13 22 31 40
  for i in range(5):
    if a[i][4-i] == 0:
      cntColD2 += 1
  if cntColD2 == 5:
    res += 1

  return res

b = list()
for _ in range(5):
  row = list(map(int, input().split()))
  b.append(row)

call = list()
for _ in range(5):
  row = list(map(int, input().split()))
  call += row

cnt = 0
for k in range(25):
  for i in range(5):
    for j in range(5):
      if call[k] == b[i][j]:
        b[i][j] = 0
        cnt += 1

  if cnt >= 12:
    if checkBingo(b) >= 3:
      print(k+1)
      break
