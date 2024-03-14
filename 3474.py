'''
문제
자연수 N이 주어지면 N!의 오른쪽 끝에 있는 0의 개수를 알려주는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어지고, 이어서 T개의 줄에 정수 N이 주어진다(1 <= N <= 1000000000).

출력
각 줄마다 N!의 오른쪽 끝에 있는 0의 개수를 출력한다.
'''

from sys import stdin
input = stdin.readline
t = int(input())
for _ in range(t):
  n = int(input())
  cnt = 0
  k = 5
  while k <= n:
    cnt += n//k
    k = k*5
  print(cnt)
