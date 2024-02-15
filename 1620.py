'''
문제

포켓몬 마스터가 되기 위해 도감을 완성시킨다. 가지고 있는 포켓몬 도감에서 포켓몬의 이름을 보면 포켓몬의 번호를 말하거나, 포켓몬의 번호를 보면 포켓몬의 이름을 말한다.

입력
첫째 줄에는 도감에 수록되어 있는 포켓몬의 개수 N이랑  맞춰야 하는 문제의 개수 M이 주어진다. N과 M은 1보다 크거나 같고, 100,000보다 작거나 같은 자연수이다.

둘째 줄부터 N개의 줄에 포켓몬의 번호가 1번인 포켓몬부터 N번에 해당하는 포켓몬까지 한 줄에 하나씩 입력으로 들어온다. 포켓몬의 이름은 모두 영어로만 이루어져있고, 첫 글자만 대문자이고, 나머지 문자는 소문자로만 이루어져 있다. 일부 포켓몬은 마지막 문자만 대문자일 수도 있다. 포켓몬 이름의 최대 길이는 20, 최소 길이는 2이다. 

그 다음 줄부터 총 M개의 줄에 내가 맞춰야하는 문제가 입력으로 들어온다. 문제가 알파벳으로만 들어오면 포켓몬 번호를 말해야 하고, 숫자로만 들어오면 번호에 해당하는 문자를 출력해야한다. 입력으로 들어오는 숫자는 반드시 1보다 크거나 같고, N보다 작거나 같고, 입력으로 들어오는 문자는 반드시 도감에 있는 포켓몬의 이름만 주어진다.

출력
첫째 줄부터 차례대로 M개의 줄에 각각의 문제에 대한 답을 말한다. 입력으로 숫자가 들어왔다면 그 숫자에 해당하는 포켓몬의 이름을, 문자가 들어왔으면 그 포켓몬의 이름에 해당하는 번호를 출력하면 된다.
'''

from sys import stdin
input = stdin.readline

N, M = map(int, input().split())

pokeDic = {}
for i in range(N):
  tmp = input().rstrip()
  pokeDic[i+1] = tmp
  pokeDic[tmp] = i+1

for _ in range(M):
  inv = input().rstrip()
  if inv.isdigit():
    print(pokeDic[int(inv)])
  else:
    print(pokeDic[inv])
