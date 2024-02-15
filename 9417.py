'''
문제
정수 M개가 주어졌을 때, 모든 두 수의 쌍 중에서 가장 큰 최대공약수 찾는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 N (1 < N < 100)이 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있으며, 양의 정수 M (1 < M < 100)개가 주어진다. 모든 수는 -2^{31}보다 크거나 같고, 2^{31} -1보다 작거나 같다. 

출력
각 테스트 케이스마다, 입력으로 주어진 수의 모든 두 수의 쌍의 최대공약수 중 가장 큰 값을 출력한다.
'''

from sys import stdin
from itertools import combinations
input = stdin.readline

def gcd(a, b):
  while b:
    a, b = b, a % b
  return a

n = int(input())
for _ in range(n):
  max = -1
  f = map(int, input().split())
  for a, b in list(combinations(f, 2)):
    g = gcd(a, b)
    if g > max:
      max = g
  print(max)
