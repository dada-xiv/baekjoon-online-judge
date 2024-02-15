'''
문제
터져 나오는 불만에 번호표 순서로만 간식을 줄 수 있다고 말했다. 
그제야 학생들이 순서대로 줄을 서려고 했지만 공간이 너무 협소해서 마음대로 이동할 수 없었다. 다행히도 대기열의 왼쪽에는 1열로 설 수 있는 공간이 존재하여 이 공간을 잘 이용하면 모두가 순서대로 간식을 받을 수 있을지도 모른다.

사람들은 현재 1열로 줄을 서있고, 맨 앞의 사람만 이동이 가능하다. 번호표 순서대로만 통과할 수 있는 라인을 만들어 두었다. 이 라인과 대기열의 맨 앞 사람 사이에는 한 사람씩 1열이 들어갈 수 있는 공간이 있다. 현재 대기열의 사람들은 이 공간으로 올 수 있지만 반대는 불가능하다.

입력
입력의 첫째 줄에는 현재 앞에 서 있는 학생들의 수 N(1 ≤ N ≤ 1,000,자연수)이 주어진다.

다음 줄에는  앞에 서있는 모든 학생들의 번호표(1,2,...,N) 순서가 앞에서부터 뒤 순서로 주어진다.

출력
무사히 간식을 받을 수 있으면 "Nice"(따옴표는 제외)를 출력하고 그렇지 않다면 "Sad"(따옴표는 제외)를 출력한다.
'''

from collections import deque
from sys import stdin
input = stdin.readline

N = int(input())
ins = list(map(int, input().split()))

tmp = deque()
cnt = 0
isNice = True
tmpN = 0
i=0
while i < N:
  if tmpN > 0 and tmp[tmpN-1] == cnt+1:
    tmp.pop()
    tmpN -= 1
    cnt += 1
  elif ins[i] == cnt+1:
    cnt += 1
    i+=1
  elif ins[i] > cnt:
    tmp.append(ins[i])
    tmpN += 1
    i+=1
  else:
    isNice = False
    break

for i in range(tmpN-1, -1, -1):
  if tmp[i] == cnt+1:
    cnt += 1
  else:
    isNice = False
    break

if isNice:
  print("Nice")
else:
  print("Sad")
