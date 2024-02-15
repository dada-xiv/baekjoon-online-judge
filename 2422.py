'''
문제
N종류의 아이스크림이 있다. 모든 아이스크림은 1부터 N까지 번호가 매겨져있다. 어떤 종류의 아이스크림을 함께 먹으면 맛이 형편없어진다. 따라서 이러한 경우를 피하면서 아이스크림을 3가지 선택하려고 한다. 이때 선택하는 방법이 몇 가지인지 구하려고 한다.

입력
첫째 줄에 정수 N과 M이 주어진다. N은 아이스크림 종류의 수이고, M은 섞어먹으면 안 되는 조합의 개수이다. 아래 M개의 줄에는 섞어먹으면 안 되는 조합의 번호가 주어진다. 같은 조합은 두 번 이상 나오지 않는다. (1 ≤ N ≤ 200, 0 ≤ M ≤ 10,000)

출력
첫째 줄에 가능한 방법이 총 몇 개 있는지 출력한다.
'''

from itertools import combinations
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
choicemap = [[True for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
  x, y = map(int, input().split())
  choicemap[x][y] = False
  choicemap[y][x] = False

cnt = 0
for li in combinations(range(1, n+1), 3):
  if choicemap[li[0]][li[1]] == False or choicemap[li[0]][li[2]] == False or choicemap[li[1]][li[2]] == False:
    continue
  cnt += 1
print(cnt)
