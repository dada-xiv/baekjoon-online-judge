'''
문제
문을 통과하려면 검문을 받아야 한다. 여러 마리의 소가 들어가려고 하면 줄이 그 만큼 길어진다. N마리의 소가 문을 통과한다. 도착한 시간과 검문받는 데 걸리는 시간은 소마다 다를 수 있고, 두 소가 동시에 검문을 받을 수 없다. 예를 들어 소 A가 5초에 도착했고 7초 동안 검문을 받으면, 8초에 도착한 그 다음 소 B는 12초까지 줄을 서야 검문을 받을 수 있다. 모든 소가 통과하려면 얼마나 걸리는 지 구해보자.

입력
첫 줄에 100 이하의 양의 정수 N이 주어진다. 다음 N줄에는 한 줄에 하나씩 소의 도착 시각과 검문 시간이 주어진다. 각각 1,000,000 이하의 양의 정수이다.

출력
모든 소가 입장하는 데 걸리는 최소 시간을 출력한다.
'''

from sys import stdin
input = stdin.readline
n = int(input())
a = []
for _ in range(n):
  aT, gT = map(int, input().split())
  a.append((aT, gT))

a.sort()
time = 0
for aT, gT in a:
  if time == 0:
    time = aT+gT
  else:
    if aT >= time:
      time = aT+gT
    else:
      time = time+gT

print(time)
