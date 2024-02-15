'''
문제
크기 N인 배열 X가 있을 때, X의 연속한 부분배열 중 원소의 합이 가장 큰 부분 배열을 찾는 Maximum subarray problem은 컴퓨터 과학에서 잘 알려져 있다.

N과 배열 X가 주어졌을 때, X의 maximum subarray의 합을 구하자. 즉, 
max_{1 ≤ i ≤ j ≤ N} (X[i]+...+X[j])를 구하자.

입력
입력 파일의 첫 번째 줄에 테스트 케이스의 수를 의미하는 자연수 T가 주어진다. 그 다음에는 T개의 테스트 케이스가 주어진다. 각 테스트케이스 별로 첫 번째 줄에 배열의 크기 N이 주어진다. (1 ≤ N ≤ 1,000)
그리고 두 번째 줄에 배열 X의 내용을 나타내는 N개의 정수가 공백으로 구분되어 주어진다. 이때 주어지는 수는 절댓값이 1,000보다 작은 정수이다.

출력
각 테스트케이스 별로 maximum subarray의 합을 줄로 구분하여 출력한다.
'''

from sys import stdin
input = stdin.readline
t = int(input())
for _ in range(t):
  n = int(input())
  a = list(map(int, input().split()))
  sumMax = n*(-1000)
  for k in range(n):
    for i in range(n-k):
      s = sum(a[i:i+k+1])
      if s > sumMax:
        sumMax = s
  print(sumMax)