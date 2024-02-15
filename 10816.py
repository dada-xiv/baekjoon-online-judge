'''
문제
숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 넷째 줄에는 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다. 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

출력
첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 몇 개 가지고 있는지를 공백으로 구분해 출력한다.
'''

from sys import stdin
input = stdin.readline

# def binarySearch(a, L, R, target):
#   while L <= R:
#     m = (L + R) // 2
#     if a[m] == target:
#       return m
#     elif a[m] > target:
#       R = m - 1
#     else:
#       L = m + 1
#   return -1

N = int(input())
nC = list(map(int, input().split()))
numCard = {}
for i in range(N):
  if nC[i] in numCard:
    numCard[nC[i]] += 1
  else:
    numCard[nC[i]] = 1

# print(numCard)

M = int(input())
a = list(map(int, input().split()))

for i in range(M):
  if a[i] in numCard:
    print(numCard[a[i]], end=' ')
  else:
    print(0, end=' ')
