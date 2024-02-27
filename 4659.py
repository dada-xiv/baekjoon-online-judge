'''
문제
비밀번호의 조건은 다음과 같다:
1. 모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
2. 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
3. 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.

입력
입력은 여러개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 테스트할 패스워드가 주어진다. 마지막 테스트 케이스는 `end`이며, 패스워드는 한글자 이상 20글자 이하의 문자열이다. 또한 패스워드는 대문자를 포함하지 않는다.

출력
각 테스트 케이스에 대하여 '예제 출력'과 같이 출력하시오.
<a> is acceptable.
<tv> is not acceptable.
'''

vowel = ['a', 'e', 'i', 'o', 'u']

def isVowel(sch):
  for e in vowel:
    if e in sch:
      return True
  return False

while True:
  isAcceptable = False
  str = input()
  if str == 'end':
    break
  lenS = len(str)
  for e in vowel:
    if e in str:
      isAcceptable = True
      break
  cntVowel = 0
  cntConsonant = 0
  if isVowel(str[0]):
    cntConsonant = 0
    cntVowel += 1
  else:
    cntVowel = 0
    cntConsonant += 1
  prevChr = str[0]
  for i in range(1, lenS):
    if isVowel(str[i]):
      cntConsonant = 0
      cntVowel += 1
    else:
      cntVowel = 0
      cntConsonant += 1
    if (cntVowel >= 3 or cntConsonant >= 3) or (str[i] == prevChr and (str[i] != 'e' and str[i] != 'o')):
      isAcceptable = False
      break
    else:
      prevChr = str[i]
  if isAcceptable:
    print(f"<{str}> is acceptable.")
  else:
    print(f"<{str}> is not acceptable.")
