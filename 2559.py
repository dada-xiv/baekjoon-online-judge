'''
문제
수열이 주어졌을 때, 연속적인 합 중 최댓값을 알아보고자 한다. 예를 들어, 아래와 같이 10개의 숫자가 주어졌을 때,

3 -2 -4 -9 0 3 7 13 8 -3

연속적인 2개의 수의 합 중에서 가장 큰 값은 21이다. 정수의 수열이 주어졌을 때, 연속적인 K개의 숫자의 합이 가장 큰 값을 계산하는 프로그램을 작성하시오.

입력
첫째 줄에는 두 개의 정수 N과 K가 한 개의 공백을 사이에 두고 순서대로 주어진다. 첫 번째 정수 N은 전체 숫자의 갯수이다. (2 ≤ N ≤ 100,000) K는 합을 구하기 위한 연속적인 수의 갯수이다. (1 ≤ K ≤ N) 둘째 줄에는 N개의 정수가 빈칸을 사이에 두고 주어진다. 이 수들은 모두 -100 이상 100 이하이다.

출력
첫째 줄에 연속적인 K개의 합 중 최댓값을 출력한다.
'''
from sys import stdin
input = stdin.readline
n, k = map(int, input().split())
a = list(map(int, input().split()))
ptsum = sum(a[:k])
max = ptsum
for i in range(1, n-k+1):
  ptsum = ptsum+a[i+k-1]-a[i-1]
  if ptsum > max:
    max = ptsum
print(max)
