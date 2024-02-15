'''
문제
참외밭은 ㄱ-자 모양이거나 ㄱ-자를 90도, 180도, 270도 회전한 모양(┏, ┗, ┛ 모양)의 육각형이다. 밭의 경계(육각형의 변)는 모두 동서 방향이거나 남북 방향이었다. 밭의 한 모퉁이에서 출발하여 밭의 둘레를 돌면서 밭경계 길이를 모두 측정하였다.

1m^2의 넓이에 자라는 참외의 개수와, 참외밭을 이루는 육각형의 임의의 한 꼭짓점에서 출발하여 반시계방향으로 둘레를 돌면서 지나는 변의 방향과 길이가 순서대로 주어진다. 이 참외밭에서 자라는 참외의 수를 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에 1m^2의 넓이에 자라는 참외의 개수를 나타내는 양의 정수 K (1 ≤ K ≤ 20)가 주어진다. 참외밭을 나타내는 육각형의 임의의 한 꼭짓점에서 출발하여 반시계방향으로 둘레를 돌면서 지나는 변의 방향과 길이 (1 이상 500 이하의 정수) 가 둘째 줄부터 일곱 번째 줄까지 한 줄에 하나씩 순서대로 주어진다. 변의 방향에서 동쪽은 1, 서쪽은 2, 남쪽은 3, 북쪽은 4로 나타낸다.

출력
첫째 줄에 입력으로 주어진 밭에서 자라는 참외의 수를 출력한다.
'''


def getIdx(n):
  if n < 0:
    n += 6
  elif n >= 6:
    n -= 6
  return n

K = int(input())
a = list()
maxIdx = 0
wD = -1
for i in range(6):
  o, v = map(int, input().split())
  if v > wD:
    wD = v
    maxIdx = i
  a.append(v)

hD = 0
mul = 0
LIdx = getIdx(maxIdx-1)
RIdx = getIdx(maxIdx+1)
if a[LIdx] < a[RIdx]:
  hD = a[RIdx]
  mul = -1
else:
  hD = a[LIdx]
  mul = 1

wd = a[getIdx(maxIdx+mul*2)]
hd = a[getIdx(maxIdx+mul*3)]

print((wD*hD-wd*hd)*K)
