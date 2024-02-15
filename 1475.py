'''
문제
플라스틱 숫자를 한 세트로 판다. 한 세트에는 0번부터 9번까지 숫자가 하나씩 들어있다. 방 번호가 주어졌을 때, 필요한 세트의 개수의 최솟값을 출력하시오. (6은 9를 뒤집어서 이용할 수 있고, 9는 6을 뒤집어서 이용할 수 있다.)

입력
첫째 줄에 방 번호 N이 주어진다. N은 1,000,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 필요한 세트의 개수를 출력한다.
'''

from sys import stdin
input = stdin.readline


def roundT(val, digits):
  return round(val+10**(-len(str(val))-1), digits)


s = input().rstrip()
p = dict()
for i in range(len(s)):
  val = int(s[i])
  if val == 6 or val == 9:
    if 6 in p:
      p[6] += 0.5
    else:
      p[6] = 0.5
  else:
    if val in p:
      p[val] += 1
    else:
      p[val] = 1

max = 0
for k in p:
  if k == 6:
    pk = int(roundT(p[k], 0))
  else:
    pk = p[k]
  if pk > max:
    max = pk

print(max)
