'''
문제
주어진 문자열을 팰린드롬으로 바꾸는 프로그램을 작성하시오.

입력
첫째 줄에 문자열이 주어진다. 알파벳 대문자로만 된 최대 50글자이다.

출력
첫째 줄에 정답을 출력한다. 만약 불가능할 때는 "I'm Sorry Hansoo"를 출력한다. 정답이 여러 개일 경우에는 사전순으로 앞서는 것을 출력한다.
'''

str = input()
chdict = dict()
for c in str:
  if c in chdict:
    chdict[c] += 1
  else:
    chdict[c] = 1

cntodd = 0
midChr = ''
outChrList = list()
for k, v in chdict.items():
  if v % 2 == 1:
    midChr = k
    cntodd += 1
  outChrList.append(k)

outChrList.sort()

if cntodd > 1:
  print("I'm Sorry Hansoo")
else:
  outstream = ''
  for c in outChrList:
    if c != midChr:
      outstream += c*int(chdict[c]//2)
    else:
      outstream += c*int((chdict[c]-1)//2)
  outstream = outstream + midChr + outstream[::-1]
  print(outstream)
