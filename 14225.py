'''
문제
수열 S가 주어졌을 때, 수열 S의 부분 수열의 합으로 나올 수 없는 가장 작은 자연수를 구하는 프로그램을 작성하시오.

예를 들어, S = [5, 1, 2]인 경우에 1, 2, 3(=1+2), 5, 6(=1+5), 7(=2+5), 8(=1+2+5)을 만들 수 있다. 하지만, 4는 만들 수 없기 때문에 정답은 4이다.

입력
첫째 줄에 수열 S의 크기 N이 주어진다. (1 ≤ N ≤ 20)

둘째 줄에는 수열 S가 주어진다. S를 이루고있는 수는 100,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 수열 S의 부분 수열의 합으로 나올 수 없는 가장 작은 자연수를 출력한다.
'''

from sys import stdin
input = stdin.readline

n = int(input())
s = list(map(int, input().split()))
s.sort()
# print(s)

sum = 0
for i in range(n):
  # print(sum+1, s[i], sum+1 < s[i])
  # 현재까지 더한 값보다 1만큼 큰 수가 다음 원소보다 작으면
  if sum+1 < s[i]:
    break
  sum += s[i]

print(sum+1)
