'''
문제
영어 단어를 외우기 위해 영어 단어장을 만들려 하고 있다. 만들고자 하는 단어장의 순서는 다음과 같은 우선순위를 차례로 적용하여 만들어진다.
1. 자주 나오는 단어일수록 앞에 배치한다.
2. 단어의 길이가 길수록 앞에 배치한다.
3. 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치한다.
M보다 짧은 길이의 단어의 경우 읽는 것만으로도 외울 수 있기 때문에 길이가 M이상인 단어들만 외운다.

입력
첫째 줄에는 영어 지문에 나오는 단어의 개수 N과 외울 단어의 길이 기준이 되는 M이 공백으로 구분되어 주어진다. (1 ≤ N ≤ 100000, 1 ≤ M ≤ 10)
둘째 줄부터 N+1번째 줄까지 외울 단어를 입력받는다. 입력은 알파벳 소문자로만 주어지며 단어의 길이는 10을 넘지 않는다.
단어장에 단어가 반드시 1개 이상 존재하는 입력만 주어진다.

출력
단어장의 앞에 위치한 단어부터 한 줄에 한 단어씩 순서대로 출력한다.
'''

from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
words = dict()
for _ in range(n):
  v = input().rstrip()
  if len(v) >= m:
    if v in words:
      words[v] += 1
    else:
      words[v] = 1

wordsArr = []
for k, v in words.items():
  wordsArr.append((k, v))
wordsArr.sort(key=lambda x: (-x[1], -len(x[0]), x[0]))

for item in wordsArr:
  print(item[0])
