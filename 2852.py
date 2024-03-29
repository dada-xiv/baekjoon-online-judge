'''
문제
농구 경기는 정확히 48분동안 진행된다. 각 팀이 몇 분동안 이기고 있었는지 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 골이 들어간 횟수 N(1<=N<=100)이 주어진다. 둘째 줄부터 N개의 줄에 득점 정보가 주어진다. 득점 정보는 득점한 팀의 번호와 득점한 시간으로 이루어져 있다. 팀 번호는 1 또는 2이다. 득점한 시간은 MM:SS(분:초) 형식이며, 분과 초가 한자리 일 경우 첫째자리가 0이다. 분은 0보다 크거나 같고, 47보다 작거나 같으며, 초는 0보다 크거나 같고, 59보다 작거나 같다. 득점 시간이 겹치는 경우는 없다.

출력
첫째 줄에 1번 팀이 이기고 있던 시간, 둘째 줄에 2번 팀이 이기고 있던 시간을 출력한다. 시간은 입력과 같은 형식(MM:SS)으로 출력한다.
'''

def secToTime(fullsec):
  min = fullsec//60
  sec = fullsec-min*60
  return '{:02}'.format(min)+':'+'{:02}'.format(sec)

n = int(input())
a = list()
prevSec = 0
score1, score2 = 0, 0
timeWin1, timeWin2 = 0, 0
for _ in range(n):
  strTeam, strTime = map(str, input().split())
  tMin, tSec = map(int, strTime.split(":"))
  curSec = tMin*60 + tSec
  timeSec = curSec-prevSec
  if score1 > score2:
    timeWin1 += timeSec
  elif score1 < score2:
    timeWin2 += timeSec
  if strTeam == "1":
    score1 += 1
  else:
    score2 += 1
  prevSec = curSec
  # print(curSec, score1, score2, timeSec)

curSec = 48*60
timeSec = curSec-prevSec
if score1 > score2:
  timeWin1 += timeSec
elif score1 < score2:
  timeWin2 += timeSec
# print(curSec, timeSec)

print(secToTime(timeWin1))
print(secToTime(timeWin2))