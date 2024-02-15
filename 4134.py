'''
문제
정수 n(0 ≤ n ≤ 4*109)가 주어졌을 때, n보다 크거나 같은 소수 중 가장 작은 소수 찾는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다.

출력
각각의 테스트 케이스에 대해서 n보다 크거나 같은 소수 중 가장 작은 소수를 한 줄에 하나씩 출력한다.
'''

import math
from sys import stdin
input = stdin.readline

def isPrime(n):
  if n < 2:
    return False
  sqrt_n = int(math.sqrt(n))
  for i in range(2, sqrt_n + 1):
    if n % i == 0:
      return False
  return True

T = int(input())
for _ in range(T):
  n = int(input())
  val = n
  while True:
    if isPrime(val):
      print(val)
      break
    else:
      val += 1
