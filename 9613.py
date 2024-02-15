'''
문제
양의 정수 n개가 주어졌을 때, 가능한 모든 쌍의 GCD의 합을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 t (1 ≤ t ≤ 100)이 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있다. 각 테스트 케이스는 수의 개수 n (1 < n ≤ 100)가 주어지고, 다음에는 n개의 수가 주어진다. 입력으로 주어지는 수는 1,000,000을 넘지 않는다.

출력
각 테스트 케이스마다 가능한 모든 쌍의 GCD의 합을 출력한다.
'''

from sys import stdin
input = stdin.readline

def getCombi(arr, n):
  res = []
  if n == 0:
    return [[]]
  for i in range(len(arr)-n+1):
    for combi in getCombi(arr[i+1:], n-1):
      res.append([arr[i]]+combi)
  return res

def getGCD(m, n):
  while n != 0:
    r = m % n
    m = n
    n = r
  return m

t = int(input())
for _ in range(t):
  sum = 0
  a = list(map(int, input().split()))
  for m, n in getCombi(a[1:], 2):
    sum += getGCD(m, n)
  print(sum)
