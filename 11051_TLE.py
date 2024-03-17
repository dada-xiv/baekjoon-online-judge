'''
문제
자연수 N과 정수 K가 주어졌을 때 이항 계수 (N, K)를 10,007로 나눈 나머지를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ K ≤ N)

출력
(N, K)를 10,007로 나눈 나머지를 출력한다.
'''

n, k = map(int, input().split())
m = 10007
def combi(n, k):
  if k == 1:
    return n % m
  elif n == k:
    return 1
  else:
    return combi(n-1, k) % m + combi(n-1, k-1) % m
print(combi(n, k))
