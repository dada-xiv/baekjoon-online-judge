'''
문제
폴리오미노 AAAA와 BB를 무한개만큼 가지고 있다. '.'와 'X'로 이루어진 보드판이 주어졌을 때, 겹침없이 'X'를 모두 폴리오미노로 덮으려고 한다. 이때, '.'는 폴리오미노로 덮으면 안 된다. 폴리오미노로 모두 덮은 보드판을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 보드판이 주어진다. 보드판의 크기는 최대 50이다.

출력
첫째 줄에 사전순으로 가장 앞서는 답을 출력한다. 만약 덮을 수 없으면 -1을 출력한다.
'''


str = input()
arr = str.split('.')
# print(arr)
res = ''
isFalse = False
for pt in arr:
  lenPt = len(pt)
  if lenPt % 2 == 1:
    isFalse = True
    break
  else:
    q = lenPt // 4
    r = lenPt % 4
    res += 'AAAA'*q+'B'*r
  res += '.'
if isFalse:
  print(-1)
else:
  print(res[:-1])
