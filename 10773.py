'''
문제
장부를 관리하는 중이다. 잘못된 수를 부를 때마다 0을 외쳐서, 가장 최근에 쓴 수를 지우게 시킨다. 이렇게 모든 수를 받아 적은 후 그 수의 합을 알고 싶어 한다.

입력
첫 번째 줄에 정수 K가 주어진다. (1 ≤ K ≤ 100,000)

이후 K개의 줄에 정수가 1개씩 주어진다. 정수는 0에서 1,000,000 사이의 값을 가지며, 정수가 "0" 일 경우에는 가장 최근에 쓴 수를 지우고, 아닐 경우 해당 수를 쓴다.
정수가 "0"일 경우에 지울 수 있는 수가 있음을 보장할 수 있다.

출력
최종적으로 적어 낸 수의 합을 출력한다. 최종적으로 적어낸 수의 합은 $2^{31}-1$보다 작거나 같은 정수이다.
'''

from collections import deque
from sys import stdin
input = stdin.readline
a = deque()
K = int(input())
for _ in range(K):
  val = int(input())
  if val ==0:
    a.pop()
  else:
    a.append(val)
print(sum(a))
