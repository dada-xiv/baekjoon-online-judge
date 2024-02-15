'''
문제
N개의 원소를 포함하고 있는 양방향 순환 que에서 몇 개의 원소를 뽑아내려고 한다. que에 대하여 다음과 같은 3가지 연산을 수행할 수 있다.

1. 첫 번째 원소를 뽑아낸다. 이 연산을 수행하면 a1, ..., ak이었던 것이 a2, ..., ak와 같이 된다.
2. 왼쪽으로 한 칸 이동시킨다. 이 연산을 수행하면 a1, ..., ak가 a2, ..., ak, a1이 된다.
3. 오른쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 ak, a1, ..., ak-1이 된다.

큐에 처음에 포함되어 있던 수 N과 뽑아내려고 하는 원소의 위치가 주어진다. (이 위치는 가장 처음 큐에서의 위치이다.) 이때, 그 원소를 주어진 순서대로 뽑아내는데 드는 2번, 3번 연산의 최솟값을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 큐의 크기 N(1≤N≤50)과 뽑아내려고 하는 수의 개수 M(1≤M≤N)이 주어진다. 둘째 줄에는 뽑아내려고 하는 수의 위치가 순서대로 주어진다. 위치는 1보다 크거나 같고, N보다 작거나 같은 자연수이다.

출력
첫째 줄에 문제의 정답을 출력한다.
'''

from collections import deque
n, m = map(int, input().split())
idx = list(map(int, input().split()))
q = deque([i for i in range(1, n+1)])

cnt = 0
for idc in idx:
  while True:
    if q[0] == idc:
      q.popleft()
      break
    else:
      if q.index(idc) < len(q)/2:
        while q[0] != idc:
          q.rotate(-1)
          cnt += 1
      else:
        while q[0] != idc:
          q.rotate(1)
          cnt += 1

print(cnt)
