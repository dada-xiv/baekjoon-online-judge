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
combi = [[1]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
  for j in range(1, i):
    combi[i][j] = combi[i-1][j] % m+combi[i-1][j-1] % m
print(combi[n][k] % m)
