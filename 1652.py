'''
문제
방은 N*N의 정사각형모양으로 생겼다. 방 안에는 옮길 수 없는 짐들이 있어서 누울 수 있는 자리를 찾아야 한다. 누울 수 있는 자리는 2칸 이상이 연속해서 한 줄로 이어진 것을 한 칸으로 친다. 가로로 누울 수도 있고 세로로 누울 수도 있다. 누울 때는 반드시 벽이나 짐에 닿아야 한다. 방의 크기 N과 방의 구조가 주어졌을 때, 가로로 누울 수 있는 자리와 세로로 누울 수 있는 자리의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 방의 크기 N이 주어진다. N은 1이상 100이하의 정수이다. 그 다음 N줄에 걸쳐 N개의 문자가 들어오는데 '.'은 아무것도 없는 곳을 의미하고, 'X'는 짐이 있는 곳을 의미한다.

출력
첫째 줄에 가로로 누울 수 있는 자리와 세로로 누울 수 있는 자리의 개수를 출력한다.
'''

n = int(input())
a = list()
for _ in range(n):
  row = list(input())
  a.append(row)

cntr, cntc = 0, 0
for i in range(n):
  lenr = 0
  lenc = 0
  for j in range(n):
    if a[i][j] == '.':
      lenr += 1
    else:
      if lenr >= 2:
        cntr += 1
      lenr = 0
    if a[j][i] == '.':
      lenc += 1
    else:
      if lenc >= 2:
        cntc += 1
      lenc = 0
    if j == n-1 and lenr >= 2:
      cntr += 1
    if j == n-1 and lenc >= 2:
      cntc += 1

print(cntr, cntc)
