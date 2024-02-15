'''
문제
걸그룹 개인과 팀의 이름을 출력하는 프로그램을 만들고자 한다.

입력
첫 번째 줄에는 총 입력 받을 걸그룹의 수 N(0 < N < 100)과 맞혀야 할 문제의 수 M(0 < M < 100)을 입력받는다.

두 번째 줄부터는 각 걸그룹마다 팀의 이름, 걸그룹의 인원 수, 멤버의 이름을 한 줄씩 차례대로 입력받는다. 팀과 멤버의 이름은 최대 100글자이며, 모든 글자는 알파벳 소문자이다. 하나의 걸그룹이나 서로 다른 두 걸그룹에 이름이 같은 두 멤버가 있는 경우는 없다.

그 다음 줄부터는 M개의 퀴즈를 입력받는다. 각각의 퀴즈는 두 줄로 이루어져 있으며, 팀의 이름이나 멤버의 이름이 첫 줄에 주어지고 퀴즈의 종류를 나타내는 0 또는 1이 두 번째 줄에 주어진다. 퀴즈의 종류가 0일 경우 팀의 이름이 주어지며, 1일 경우 멤버의 이름이 주어진다.

출력
첫 번째 줄부터 차례대로 퀴즈에 대한 답을 출력한다. 퀴즈의 종류가 0일 경우 해당 팀에 속한 멤버의 이름을 사전순으로 한 줄에 한 명씩 출력한다. 퀴즈의 종류가 1일 경우 해당 멤버가 속한 팀의 이름을 출력한다.
'''

from sys import stdin
input = stdin.readline
n, m = map(int, input().split())
grp = {}
for _ in range(n):
  teamName = input().rstrip()
  grp[teamName] = set()
  memberN = int(input())
  for _ in range(memberN):
    name = input().rstrip()
    grp[teamName].add(name)

for _ in range(m):
  name = input().rstrip()
  quiz = int(input())
  if quiz == 0:
    klist = list(grp[name])
    klist.sort()
    for m in klist:
      print(m)
  elif quiz == 1:
    for tName in grp:
      if name in grp[tName]:
        print(tName)
        break
