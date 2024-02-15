'''
문제
n개의 정수로 이루어진 임의의 수열이 주어진다. 이 중 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합을 구하려고 한다. 단, 수는 한 개 이상 선택해야 한다.

예를 들어서 10, -4, 3, 1, 5, 6, -35, 12, 21, -1 이라는 수열이 주어졌다고 하자. 여기서 정답은 12+21인 33이 정답이다.

입력
첫째 줄에 정수 n(1 ≤ n ≤ 100,000)이 주어지고 둘째 줄에는 n개의 정수로 이루어진 수열이 주어진다. 수는 -1,000보다 크거나 같고, 1,000보다 작거나 같은 정수이다.

출력
첫째 줄에 답을 출력한다.
'''

from sys import stdin
input = stdin.readline

n = int(input())
a = list(map(int, input().split()))
# print(a)

sumd = dict()
for i in range(n):
  sumd[(i, i)] = a[i]
  # print(f"({i},{i})", end=' ')
# print()

# print(sumd)
max = a[0]
for i in range(2, n+1):
  # print(f"{i}: ", end='')
  for j in range(n-i+1):
    # print(f"({j},{j+i-1})=({j},{j+i-2})+({j+i-1},{j+i-1})", end=' ')
    val = sumd[j, j+i-2]+a[j+i-1]
    sumd[j, j+i-1] = val
    if val > max:
      max = val
  # print()

print(max)
