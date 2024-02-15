'''
문제
점프 게임의 조건은 다음과 같다:

1. 가로와 세로의 칸 수가 같은 정사각형의 구역 내부에서만 움직일 수 있다. 정사각형 구역의 외부로 나가는 경우엔 바닥으로 떨어져 즉시 게임에서 패배하게 된다.
2. 출발점은 항상 정사각형의 가장 왼쪽, 가장 위의 칸이다. 다른 출발점에서는 출발하지 않는다.
3. 이동 가능한 방향은 오른쪽과 아래 뿐이다. 위쪽과 왼쪽으로는 이동할 수 없다.
4. 가장 오른쪽, 가장 아래 칸에 도달하는 순간 '승리'로 게임은 종료된다.
5. 한 번에 이동할 수 있는 칸의 수는 현재 밟고 있는 칸에 쓰여 있는 수 만큼이다.

주어진 게임판에서 끝 점(오른쪽 맨 아래 칸)까지 도달할 수 있는지를 알아보자.

입력
입력의 첫 번째 줄에는 게임 구역의 크기 N (2 ≤ N ≤ 3)이 주어진다.
입력의 두 번째 줄부터 마지막 줄까지 게임판의 구역(맵)이 주어진다.
게임판의 승리 지점(오른쪽 맨 아래 칸)에는 -1이 쓰여있고, 나머지 칸에는 0 이상 100 이하의 정수가 쓰여있다.

출력
끝 점에 도달할 수 있으면 'HaruHaru'(인용부호 없이), 도달할 수 없으면 'Hing'을 한 줄에 출력한다.
'''

n = int(input())
a = []
for _ in range(n):
  a.append(list(map(int, input().split())))

def getNextStep(i, j):
  if i >= n or j >= n:
    return False
  curStep = a[i][j]
  # print(i, j, a[i][j])
  if curStep == -1:
    return True
  elif curStep == 0:
    return False
  else:
    return getNextStep(i + curStep, j) or getNextStep(i, j + curStep)

if getNextStep(0, 0):
  print("HaruHaru")
else:
  print("Hing")
