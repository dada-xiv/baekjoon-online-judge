'''
문제
예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

입력
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

출력
첫째 줄부터 차례대로 별을 출력한다.
'''


def incCage(a):
  lenA = len(a)
  nA = int((lenA+3)/4)
  for i in range(lenA):
    a[i] = '* '+a[i]+' *'
  row = '*'
  for _ in range(lenA+2):
    row += ' '
  row += '*'
  a = [row]+a+[row]
  row = ''
  for _ in range(lenA+4):
    row += '*'
  a = [row]+a+[row]
  return a

n = int(input())
a = ['*']

for _ in range(n-1):
  a = incCage(a)

for i in range(len(a)):
  print(a[i])
