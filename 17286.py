'''
문제
고양이와 세 사람은 이차원 좌표평면 위에 있다. 좌표평면 상의 좌표는 (x, y)로 나타낼 수 있다. 고양이는 세 사람 모두에게 안기려고 한다. 고양이가 안기려면 사람이 있는 위치로 이동해야 한다. 사람은 이동하지 않는다. 고양이는 최단 거리로 세 사람에게 이동하려고 한다.

예를 들어, 고양이의 위치가 (0, 0) 세 사람의 위치가 각각 (1, 0), (2, 0), (4, 0)인 경우에, (0, 0) → (1, 0) → (2, 0) → (4, 0)으로 이동하면 최단 거리로 이동할 수 있다. 이때, 거리는 1 + 1 + 2 = 4이다.

고양이와 세 사람의 위치가 주어진다. 세 사람 모두에게 안기는 최단 거리를 구하시오.

입력
첫째 줄에 고양이의 위치, 둘째 줄부터 세 개의 줄에 사람의 위치가 한 줄에 하나씩 주어진다. 위치는 x, y좌표의 순서로 주어지며, 공백으로 구분되어져 있다. (-10 ≤ x, y ≤ 10)

한 위치에 둘 이상의 사람이 있는 경우는 없고, 고양이와 사람의 위치가 같은 경우도 없다.

출력
첫째 줄에 고양이의 최단 거리를 출력한다. 소수점 이하는 버리고 정수만 출력한다.
'''


import math

def getPerm(arr, n):
  res = []
  if n == 0:
    return [[]]
  for i in range(len(arr)):
    for rest in getPerm(arr[:i]+arr[i+1:], n-1):
      res.append([arr[i]]+rest)
  return res

def dist2t(t1, t2):
  return math.sqrt((t1[0]-t2[0])**2+(t1[1]-t2[1])**2)

Ox, Oy = map(int, input().split())
catP = (Ox, Oy)
humanP = list()
for _ in range(3):
  x, y = map(int, input().split())
  humanP.append((x, y))

minJouney = 100
for subp in getPerm(humanP, 3):
  pivot = catP
  journey = 0
  for t in subp:
    d = dist2t(pivot, t)
    journey += d
    pivot = t
    # print(d, end=' ')
  # print(subp, journey)
  if journey < minJouney:
    minJouney = journey
print(math.floor(minJouney))
