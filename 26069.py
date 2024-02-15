'''
문제
사람들이 만난 기록이 시간 순서대로 N개 주어진다. 댄스를 추지 않고 있던 사람이 댄스를 추고 있던 사람을 만나게 된다면, 만난 시점 이후로 댄스를 추게 된다. 기록이 시작되기 이전 댄스를 추고 있는 사람은 한 명 뿐이라고 할 때, 마지막 기록 이후 무지개 댄스를 추는 사람이 몇 명인지 구해보자!

입력
첫번째 줄에는 사람들이 만난 기록의 수 N (1 ≤ N ≤ 1000)이 주어진다.
두번째 줄부터 N개의 줄에 걸쳐 사람들이 만난 기록이 주어진다. i+1번째 줄에는 i번째로 만난 사람들의 이름 A_i와 B_i가 공백을 사이에 두고 주어진다. A_i와 B_i는 숫자와 영문 대소문자로 이루어진 최대 길이 20의 문자열이며, 서로 같지 않다.
첫 번째 사람의 이름은 ChongChong으로 주어지며, 기록에서 1회 이상 주어진다.동명이인은 없으며, 사람의 이름은 대소문자를 구분한다. (ChongChong과 chongchong은 다른 이름이다.)

출력
마지막 기록 이후 댄스를 추는 사람의 수를 출력하라.
'''

from sys import stdin
input = stdin.readline
n = int(input())
data = set()
danceStarted = False

for _ in range(n):
  a, b = map(str, input().split())
  if danceStarted == False and (a == 'ChongChong' or b == 'ChongChong'):
    data.add(a)
    data.add(b)
    danceStarted = True
  if danceStarted:
    if a in data or b in data:
      data.add(a)
      data.add(b)

print(len(data))
