'''
문제
종이에는 숫자와 알파벳 소문자로 되어있는 글자가 N줄 있다. 여기서 숫자를 모두 찾은 뒤 비내림차순으로 정리해야한다. 숫자의 앞에 0이 있는 경우에는 생략할 수 있다. 예를 들어, 01a2b3456cde478에서 숫자를 찾으면 1, 2, 3456, 478이다.

입력
첫째 줄에 줄의 개수 N이 주어진다. (1 ≤ N ≤ 100) 다음 N개의 줄에는 각 줄의 내용이 주어진다. 각 줄은 최대 100글자이고, 항상 알파벳 소문자와 숫자로만 이루어져 있다.

출력
종이에서 찾은 숫자의 개수를 M이라고 하면, 출력은 M줄로 이루어져야 한다. 각 줄에는 찾은 숫자를 하나씩 출력해야 한다. 이때, 비내림차순으로 출력해야 한다. 비내림차순은 다음 수가 앞의 수보다 크거나 같은 경우를 말한다.
'''

from sys import stdin
input = stdin.readline
n = int(input())

curnum = ''
res = []
for _ in range(n):
  curnum = ''
  feed = input().rstrip()
  for char in feed:
    if char.isdigit():
      curnum += char
    elif curnum: #if non-empty
      res.append(int(curnum))
      curnum = ''
  if curnum: #ending number
    res.append(int(curnum))

res.sort()
for num in res:
  print(num)