'''
문제
Junhee는 설문조사를 하여 자기가 귀여운지 아닌지 알아보기로 했다.

입력
첫 번째 줄에 설문조사를 한 사람의 수 N (1 ≤ N ≤ 101, N은 홀수)가 주어진다.
다음 N개의 줄에는 각 줄마다 각 사람이 설문 조사에 어떤 의견을 표명했는지를 나타내는 정수가 주어진다. 0은 귀엽지 않다고 했다는 뜻이고, 1은 귀엽다고 했다는 뜻이다.

출력
귀엽지 않다는 의견이 더 많을 경우 "Junhee is not cute!"를 출력하고 귀엽다는 의견이 많을 경우 "Junhee is cute!"를 출력하라.
'''

from sys import stdin
input = stdin.readline
n = int(input())
a = list()
for _ in range(n):
  a.append(int(input()))
if 2*sum(a)>n:
  print("Junhee is cute!")
else:
  print("Junhee is not cute!")

