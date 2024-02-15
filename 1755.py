'''
문제
79를 영어로 읽되 숫자 단위로 하나씩 읽는다면 "seven nine"이 된다. 80은 마찬가지로 "eight zero"라고 읽는다. 79는 80보다 작지만, 영어로 숫자 하나씩 읽는다면 "eight zero"가 "seven nine"보다 사전순으로 먼저 온다.

문제는 정수 M, N(1 ≤ M ≤ N ≤ 99)이 주어지면 M 이상 N 이하의 정수를 숫자 하나씩 읽었을 때를 기준으로 사전순으로 정렬하여 출력하는 것이다.

입력
첫째 줄에 M과 N이 주어진다.

출력
M 이상 N 이하의 정수를 문제 조건에 맞게 정렬하여 한 줄에 10개씩 출력한다.
'''

numToStr = dict()
numToStr[0] = "zero"
numToStr[1] = "one"
numToStr[2] = "two"
numToStr[3] = "three"
numToStr[4] = "four"
numToStr[5] = "five"
numToStr[6] = "six"
numToStr[7] = "seven"
numToStr[8] = "eight"
numToStr[9] = "nine"
strToNum = dict()
strToNum["zero"] = "0"
strToNum["one"] = "1"
strToNum["two"] = "2"
strToNum["three"] = "3"
strToNum["four"] = "4"
strToNum["five"] = "5"
strToNum["six"] = "6"
strToNum["seven"] = "7"
strToNum["eight"] = "8"
strToNum["nine"] = "9"

a = list()
m, n = map(int, input().split())
for i in range(m, n+1):
  if i < 10:
    a.append(numToStr[i])
  else:
    si = str(i)
    a.append(numToStr[int(si[0])]+" "+numToStr[int(si[1])])
a.sort()
lenA = n-m+1
for i in range(lenA):
  li = a[i].split()
  sr = ""
  for ei in li:
    sr += strToNum[ei]
  print(sr, end='')
  if (i+1)//10 == (i+1)/10:
    print()
  elif i < lenA-1:
    print(' ', end='')
