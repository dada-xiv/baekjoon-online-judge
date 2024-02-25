'''
문제
ROT13은 영어 알파벳을 13글자씩 밀어서 만든다. ROT13은 알파벳 대문자와 소문자에만 적용할 수 있다. 알파벳이 아닌 글자는 원래 글자 그대로 남아 있어야 한다. 문자열이 주어졌을 때, "ROT13"으로 암호화한 다음 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 알파벳 대문자, 소문자, 공백, 숫자로만 이루어진 문자열 S가 주어진다. S의 길이는 100을 넘지 않는다.

출력
첫째 줄에 S를 ROT13으로 암호화한 내용을 출력한다.
'''


s = input()
lenS = len(s)
res = ''
for i in range(lenS):
  ordN = ord(s[i])
  if ordN >= 65 and ordN <= 90:
    ordN += 13
    if ordN > 90:
      ordN -= 26
    res += chr(ordN)
  elif ordN >= 97 and ordN <= 122:
    ordN += 13
    if ordN > 122:
      ordN -= 26
    res += chr(ordN)
  else:
    res += s[i]
print(res)
