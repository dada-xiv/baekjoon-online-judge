'''
문제
단어 위로 아치형 곡선을 그어 같은 글자끼리(A는 A끼리, B는 B끼리) 쌍을 짓기로 하였다. 만약 선끼리 교차하지 않으면서 각 글자를 정확히 한 개의 다른 위치에 있는 같은 글자와 짝 지을수 있다면, 그 단어는 '좋은 단어'이다. '좋은 단어' 개수를 세는 프로그램을 작성하시오.

입력
첫째 줄에 단어의 수 N이 주어진다. (1 ≤ N ≤ 100)

다음 N개 줄에는 A와 B로만 이루어진 단어가 한 줄에 하나씩 주어진다. 단어의 길이는 2와 100,000사이이며, 모든 단어 길이의 합은 1,000,000을 넘지 않는다.

출력
첫째 줄에 좋은 단어의 수를 출력한다.
'''

from sys import stdin
input = stdin.readline
N = int(input())
cnt = 0
for _ in range(N):
  ins = input().rstrip()
  stck = []
  for s in ins:
    if s == 'A':
      if len(stck) > 0 and stck[-1] == 'A':
        stck.pop()
      else:
        stck.append(s)
    elif s == 'B':
      if len(stck) > 0 and stck[-1] == 'B':
        stck.pop()
      else:
        stck.append(s)
  # print(stck)
  if len(stck) == 0:
    cnt += 1

print(cnt)
