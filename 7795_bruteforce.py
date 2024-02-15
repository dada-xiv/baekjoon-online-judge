'''
문제
A={8, 1, 7, 3, 1}, B={3, 6, 1}이고 a∈A, b∈B일 때, a>b인 쌍의 개수는 8-3, 8-6, 8-1, 7-3, 7-6, 7-1, 3-1의 7가지가 있다. A와 B의 크기가 주어졌을 때, a>b인 쌍의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스의 첫째 줄에는 A의 수 N과 B의 수 M이 주어진다. 둘째 줄에는 A의 크기가 모두 주어지며, 셋째 줄에는 B의 크기가 모두 주어진다. 크기는 양의 정수이다. (1 ≤ N, M ≤ 20,000) 

출력
각 테스트 케이스마다, A가 B보다 큰 쌍의 개수를 출력한다.
'''

from sys import stdin
input = stdin.readline
t = int(input())
for _ in range(t):
  nA, nB = map(int, input().split())
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))
  a.sort(reverse=True)
  b.sort(reverse=True)
  # print(a, b)
  cnt = 0
  pivot = 0
  for i in range(nA):
    for j in range(pivot, nB):
      if a[i] > b[j]:
        pivot = j
        break
      elif j < nB-1:
        j += 1
    if a[i] > b[pivot]:
      # print(a[i], b[pivot], nB-pivot)
      cnt += (nB-pivot)
  print(cnt)
