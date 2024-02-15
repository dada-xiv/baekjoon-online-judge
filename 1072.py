'''
문제
게임 기록은 다음과 같이 생겼다. 플레이어는 이후의 모든 게임에서 지지 않는다고 가정한다.

- 게임 횟수 : X (1 ≤ X ≤ 1,000,000,000)
- 이긴 게임 : Y (0 ≤ Y ≤ X)
- 승률 : Z (단위는 %이며, 소수점은 버린다. 예를 들어, X=53, Y=47이라면, Z=88이다.)

X와 Y가 주어졌을 때, 게임을 최소 몇 번 더 해야 Z가 변하는지 구하는 프로그램을 작성하시오.

입력
각 줄에 정수 X와 Y가 주어진다.

출력
첫째 줄에 게임을 최소 몇 판 더 해야하는지 출력한다. 만약 Z가 절대 변하지 않는다면 -1을 출력한다.
'''

x, y = map(int, input().split())
winratio = y*100//x
start = 1
end = x
res = 1
if winratio >= 99:
  print(-1)
else:
  while start <= end:
    i = (start + end) // 2
    newratio = (y+i)*100//(x+i)
    if newratio > winratio:
      res = i
      end = i-1
    else:
      start = i+1
  print(res)
