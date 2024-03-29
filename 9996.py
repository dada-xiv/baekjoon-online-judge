'''
문제
패턴은 알파벳 소문자 여러 개와 별표(*) 하나로 이루어진 문자열이다.

파일 이름이 패턴에 일치하려면, 패턴에 있는 별표를 알파벳 소문자로 이루어진 임의의 문자열로 변환해 파일 이름과 같게 만들 수 있어야 한다. 별표는 빈 문자열로 바꿀 수도 있다. 예를 들어, "abcd", "ad", "anestonestod"는 모두 패턴 "a*d"와 일치한다. 하지만, "bcd"는 일치하지 않는다.

패턴과 파일 이름이 모두 주어졌을 때, 각각의 파일 이름이 패턴과 일치하는지 아닌지를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 파일의 개수 N이 주어진다. (1 ≤ N ≤ 100) 둘째 줄에는 패턴이 주어진다. 패턴은 알파벳 소문자와 별표(아스키값 42) 한 개로 이루어져 있다. 문자열의 길이는 100을 넘지 않으며, 별표는 문자열의 시작과 끝에 있지 않다. 다음 N개 줄에는 파일 이름이 주어진다. 파일 이름은 알파벳 소문자로만 이루어져 있고, 길이는 100을 넘지 않는다.

출력
총 N개의 줄에 걸쳐서, 입력으로 주어진 i번째 파일 이름이 패턴과 일치하면 "DA", 일치하지 않으면 "NE"를 출력한다.
'''

from sys import stdin
input = stdin.readline
n = int(input())
ptn = input()
sid = ptn.find('*')
ptn1 = ptn[:sid]
ptn2 = ptn[sid+1:]
lenPtn1 = len(ptn1)
lenPtn2 = len(ptn2)
for _ in range(n):
  pstr = input()
  if len(pstr) < lenPtn1+lenPtn2:
    print("NE")
  else:
    if pstr[:lenPtn1] == ptn1 and pstr[-lenPtn2:] == ptn2:
      print("DA")
    else:
      print("NE")
