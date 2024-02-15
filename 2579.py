'''
문제
계단 오르기 게임은 계단 아래 시작점부터 계단 꼭대기에 위치한 도착점까지 가는 게임이다. 각각의 계단에는 일정한 점수가 쓰여 있는데 계단을 밟으면 그 계단에 쓰여 있는 점수를 얻게 된다.

예) 시작 - 10 - 20 - 15 - 25 - 10 - 20

예를 들어 다음과 같이 시작점에서부터 첫 번째, 두 번째, 네 번째, 여섯 번째 계단을 밟아 도착점에 도달하면 총 점수는 10 + 20 + 25 + 20 = 75점이 된다.

예) 시작 -[10]-[20]- 15 -[25]- 10 -[20]

계단을 오르는 데는 다음과 같은 규칙이 있다:
1. 계단은 한 번에 한 계단 or 두 계단씩 오를 수 있다.
2. 세 개의 계단을 연속으로 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
3. 마지막 도착 계단은 반드시 밟아야 한다.

각 계단에 쓰여 있는 점수가 주어질 때 이 게임에서 얻을 수 있는 점수의 최댓값을 구하는 프로그램을 작성하시오.

입력
입력의 첫째 줄에 계단의 개수가 주어진다.
둘째 줄부터 한 줄에 하나씩 제일 아래에 놓인 계단부터 순서대로 각 계단에 쓰여 있는 점수가 주어진다. 계단의 개수는 300이하의 자연수이고, 계단에 쓰여 있는 점수는 10,000이하의 자연수이다.

출력
첫째 줄에 얻을 수 있는 점수의 최댓값을 출력한다.
'''

from sys import stdin
input = stdin.readline

T = int(input())
a = [0]
for _ in range(T):
  a.append(int(input()))

m = [0 for _ in range(T+1)]
m[0] = 0
m[1] = a[1]
if T >= 2:
  m[2] = a[1]+a[2]
if T >= 3:
  for i in range(3, T+1):
    m[i] = max(m[i-3]+a[i-1]+a[i], m[i-2]+a[i])

print(m[-1])
