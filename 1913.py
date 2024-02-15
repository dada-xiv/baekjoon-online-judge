'''
문제
홀수인 자연수 N이 주어지면, 다음과 같이 1부터 N2까지의 자연수를 달팽이 모양으로 N×N의 표에 채울 수 있다.

25	10	11	12	13
24	9	2	3	14
23	8	1	4	15
22	7	6	5	16
21	20	19	18	17

N이 주어졌을 때, 이러한 표를 출력하는 프로그램을 작성하시오. 또한 N2 이하의 자연수가 하나 주어졌을 때, 그 좌표도 함께 출력하시오. 예를 들어 N=5인 경우 6의 좌표는 (4,3)이다.

입력
첫째 줄에 홀수인 자연수 N(3 ≤ N ≤ 999)이 주어진다. 둘째 줄에는 위치를 찾고자 하는 N2 이하의 자연수가 하나 주어진다.

출력
N개의 줄에 걸쳐 표를 출력한다. 각 줄에 N개의 자연수를 한 칸씩 띄어서 출력하면 되며, 자릿수를 맞출 필요가 없다. N+1번째 줄에는 입력받은 자연수의 좌표를 나타내는 두 정수를 한 칸 띄어서 출력한다.
'''

from collections import deque
a = deque()
a.append([1])

n = int(input())
num = int(input())
kmax = int((n-1)/2)

for k in range(1, kmax+1):
  # k = 1
  n = 2*k+1
  for i in range(len(a)):
    row = list()
    row.append(n**2-i-1)
    row += a[i]
    row += [(2*k-1)**2+n+i]
    # print(row)
    a[i] = row

  rowtop = list()
  rowtop.append(n**2)
  for i in range(1, n):
    rowtop.append((2*k-1)**2+i)
  # print(rowtop)
  a.appendleft(rowtop)

  rowbtm = list()
  for i in range(n):
    rowbtm.append(n**2-n-i+1)
  # print(rowbtm)
  a.append(rowbtm)

for i in range(n):
  print(' '.join(map(str, a[i])))

for i in range(n):
  for j in range(n):
    if a[i][j] == num:
      print(i+1, j+1)
