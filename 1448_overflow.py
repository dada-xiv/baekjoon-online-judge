'''
문제
N개의 빨대 중에 3개의 빨대를 선택해서 삼각형을 만들 수 있는 조합 중 세 변의 길이의 합의 최댓값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 빨대의 개수 N이 주어진다. N은 3보다 크거나 같고, 1,000,000보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 빨대의 길이가 한 줄에 하나씩 주어진다. 빨대의 길이는 1,000,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 삼각형 세 변의 길이의 합의 최댓값을 출력한다. 만약 삼각형을 만들 수 없으면 -1을 출력한다.
'''

from itertools import combinations
from sys import stdin

def isTriangle(a, b, c):
  if a+b > c and b+c > a and c+a > b:
    return True
  else:
    return False

input = stdin.readline
n = int(input())
a = list()
for _ in range(n):
  a.append(int(input()))

max = -1
for t in list(combinations(a, 3)):
  if isTriangle(t[0], t[1], t[2]):
    sumT = sum(t)
    if sumT > max:
      max = sumT

print(max)