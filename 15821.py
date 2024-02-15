'''
문제
낚싯줄을 최대한 멀리 보낼 수 있는 거리를 낚시 거리라고 하며, 낚시 거리를 반지름으로 원을 그렸을 때 모든 영역이 원의 내부에 포함되는 낚시터를 유효 낚시터라고 한다.

현재 위치를 Z(0, 0)이라고 하자. 다각형 모양으로 생긴 각 낚시터들의 외곽선 정보가 입력으로 주어질 때, 주띵이가 K개 이상의 유효 낚시터를 확보하기 위한 최소의 낚시 거리를 계산해주자.

입력
첫 줄에는 현재 존재하는 낚시터의 수를 나타내는 자연수 N과 요구하는 최소의 유효 낚시터의 수 K가 주어진다. N과 K는 모두 10만 이하의 자연수며 K는 항상 N이하의 값을 가진다. 
이후 총 N개의 낚시터에 대한 정보가 차례로 주어진다. 각 낚시터의 정보는 두 줄로 구성되어 있다.

첫 줄에는 낚시터를 나타내는 도형의 꼭짓점 수를 나타내는 자연수 Pi가 입력으로 주어진다.
두 번째 줄에는 해당 낚시터의 꼭짓점들의 좌표가 공백으로 구분되어 주어지며, 각 좌표는 x y형식으로 주어진다. 모든 좌표는 첫 번째 점을 기준으로 시계방향 혹은 반시계방향으로 주어진다. 모든 좌표는 정수이다.
각 낚시터가 서로 겹치는 경우는 없으며, 각 낚시터는 항상 넓이가 0보다 큰 다각형이며 서로 교차하지 않는다.

출력
최소 k개의 유효 낚시터를 확보할 수 있는 최소의 낚시 거리를 계산한 후, 이를 제곱한 값을 출력한다. 소수점 세 번째 자리에서 반올림하여 두 번째 자리까지 출력한다.

Small (50점)
1 ≤ K ≤ N ≤ 100
3 ≤ Pi ≤ 10
-100 ≤ x, y ≤ 100
모든 낚시터는 볼록 다각형이다. 볼록 다각형이란, 도형의 모든 내각이 항상 180도 이하가 되는 다각형이다.

Large (50점)
1 ≤ K ≤ N ≤ 100,000
3 ≤ Pi ≤ 20
-100,000 ≤ x, y ≤ 100,000
'''

from sys import stdin
input = stdin.readline
n, k = map(int, input().split())

dist = list()
for _ in range(n):
  pN = int(input())
  a = list(map(int, input().split()))
  dmax = -1
  for i in range(pN):
    d = a[2*i]**2+a[2*i+1]**2
    # print(f"({a[2*i]}, {a[2*i+1]}):{d}", end=', ')
    if d > dmax:
      dmax = d
  dist.append(dmax)
  # print(dmax)

dist.sort()
# print(dist)
print(format(dist[k-1], ".2f"))
