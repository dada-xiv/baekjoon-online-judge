'''
문제
사람들은 원형으로 앉은 뒤 종이 위에 자신의 이름을 적는다. 다음 각자의 종이를 자기 왼편으로 전달한다. 종이를 전달받았으면, 종이 맨 위에 쓰인 이름을 가진 사람에 대해 Positive 또는 Negative 메시지를 써준다. 메시지는 종이 아래쪽에 적으며, 적은 뒤에는 종이를 접어 가린다. 다음으로 종이를 왼편으로 넘기고 같은 활동을 반복한다. 자신의 이름이 맨 위에 적힌 종이를 받으면 활동을 종료하고 각자 다른 사람들이 자기에게 남긴 메시지들을 읽어본다. Negative 말을 적은 사람을 찾아내자.

입력
입력은 번호를 가진 그룹들로 이루어져 있다. 그룹의 번호는 1부터 시작하며 1씩 증가한다. 각 그룹의 입력은 참여한 사람들의 수 n(5 ≤ n ≤ 20)이 한 줄에 주어지면서 시작된다. 
다음 n 줄에 걸쳐 위 활동을 끝마친 종이 n장이 입력된다. n 줄의 순서는 사람들이 앉아있고 종이를 넘기던 순서와 같다: 첫 번째 줄에 해당하는 사람은 두 번째 줄에 해당하는 사람에게 종이를 넘겼고, 마지막 줄에 해당하는 사람은 첫 번째 줄에 해당하는 사람에게 종이를 넘겼다.
각 줄은 종이 맨 위의 이름으로 시작한다. 다음으로 공백을 사이에 두고 종이에 적힌 메시지가 종이 위에서부터 아래로 순서대로 쓰인다. 좋은 메시지는 'P'로, 나쁜 메시지는 'N'으로 표기한다. 이름은 60글자 이하의 알파벳 소문자 또는 대문자로 이루어져 있다.
마지막 줄에 '0'이 입력되면서 입력이 종료된다. '0'은 처리하지 않는다.

출력
그룹 번호를 "Group 1"과 같이 출력함으로써 출력을 시작한다. 그 다음 줄부터 누가(A) 누구(B)에게 나쁜 말을 했는지 "A was nasty about B"로 한 줄씩 출력한다. 나쁜 말이 여러 개라면, 입력받은 순서대로─첫 번째 종이부터, 왼쪽에서 오른쪽으로─출력한다. 아무도 나쁜 말을 하지 않았다면 "Nobody was nasty"를 출력한다.
각 그룹을 빈 줄로 구분한다.
'''

from collections import deque
from sys import stdin
input = stdin.readline


def findWho(name, i, j):
  ndeq = deque(name)
  ndeq.remove(name[i])
  return ndeq[i-j-1]


cnt = 0
while True:
  n = int(input())
  if n == 0:
    break
  cnt += 1
  if cnt > 1:
    print()
  print(f"Group {cnt}")

  name = []
  nasty = []
  for _ in range(n):
    tmp = list(map(str, input().split()))
    name.append(tmp[0])
    nasty.append(tmp[1:n])

  isBadWord = False
  for i in range(n):
    for j in range(n-1):
      if nasty[i][j] == 'N':
        isBadWord = True
        print(f"{findWho(name,i,j)} was nasty about {name[i]}")
  if isBadWord == False:
    print("Nobody was nasty")
