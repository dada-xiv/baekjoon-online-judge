'''
문제
1부터 8까지 정수 8개로 이루어진 숫자에 대하여 순열 (3, 2, 7, 8, 1, 4, 5, 6)을 이용해 순열 사이클을 나타낼 수 있다. 이 순열 사이클
1 2 3 4 5 6 7 8
3 2 7 8 1 4 5 6
에는 1→3→7→5→1, 2→2, 4→8→6→4의 총 3개의 사이클이 있다. 

N개의 정수로 이루어진 순열이 주어졌을 때, 순열 사이클의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스의 첫째 줄에는 순열의 크기 N (2 ≤ N ≤ 1,000)이 주어진다. 둘째 줄에는 순열이 주어지며, 각 정수는 공백으로 구분되어 있다.

출력
각 테스트 케이스마다, 입력으로 주어진 순열에 존재하는 순열 사이클의 개수를 출력한다.
'''

from sys import stdin
input = stdin.readline
t = int(input())

for _ in range(t):
  n = int(input())
  p = [0]
  p += map(int, input().split())
  # print(p)
  pv = [True]
  pv += [False for _ in range(n)]
  cnt = 0
  while True:
    try:
      start = pv.index(False)
    except ValueError:
      break
    cidx = start
    nidx = -1
    while nidx != start:
      pv[cidx] = True
      nidx = p[cidx]
      # print(cidx, nidx)
      cidx = nidx
    cnt += 1
  print(cnt)
