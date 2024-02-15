'''
문제
숫자 카드 N장 각각에는 정수가 적혀있는데, 적혀있는 수는 -2^62보다 크거나 같고, 2^62보다 작거나 같다.

가지고 있는 카드가 주어졌을 때, 가장 많이 가지고 있는 정수를 구하는 프로그램을 작성하시오. 만약, 가장 많이 가지고 있는 정수가 여러 가지라면, 작은 것을 출력한다.

입력
첫째 줄에 숫자 카드의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개 줄에는 숫자 카드에 적혀있는 정수가 주어진다.

출력
첫째 줄에 가장 많이 가지고 있는 정수를 출력한다.
'''

from sys import stdin
input = stdin.readline
n = int(input())
a = dict()
max = 0
for _ in range(n):
  num = int(input())
  if num not in a:
    a[num] = 1
  else:
    a[num] += 1
  if a[num] > max:
    max = a[num]

b=list()
for k,v in a.items():
  if v==max:
    b.append(k)

b.sort()
print(b[0])