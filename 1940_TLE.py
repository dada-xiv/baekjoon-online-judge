'''
문제
갑옷을 만드는 재료들은 각각 고유한 번호를 가지고 있다. 갑옷은 두 개의 재료로 만드는데 두 재료의 고유한 번호를 합쳐서 M(1 ≤ M ≤ 10,000,000)이 되면 갑옷이 만들어 지게 된다. N(1 ≤ N ≤ 15,000) 개의 재료와 M이 주어졌을 때 몇 개의 갑옷을 만들 수 있는지를 구하는 프로그램을 작성하시오.

입력
첫째 줄에는 재료의 개수 N(1 ≤ N ≤ 15,000)이 주어진다. 그리고 두 번째 줄에는 갑옷을 만드는데 필요한 수 M(1 ≤ M ≤ 10,000,000) 주어진다. 그리고 마지막으로 셋째 줄에는 N개의 재료들이 가진 고유한 번호들이 공백을 사이에 두고 주어진다. 고유한 번호는 100,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 갑옷을 만들 수 있는 개수를 출력한다.
'''

from sys import stdin
input = stdin.readline
n = int(input())
m = int(input())
a = list(map(int, input().split()))
a.sort()
# print(a)

cnt = 0
isEnd = False
for i in range(n-1):
  # print(a[i], end=":")
  for j in range(i+1, n):
    # print(a[j], end=" ")
    if a[i]+a[j] == m:
      # print(f"({a[i]}, {a[j]})")
      cnt += 1
      if i+1 == j:
        isEnd = True
      break
  if isEnd:
    break
  # print()

print(cnt)