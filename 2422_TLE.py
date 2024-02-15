'''
문제
N종류의 아이스크림이 있다. 모든 아이스크림은 1부터 N까지 번호가 매겨져있다. 어떤 종류의 아이스크림을 함께 먹으면 맛이 형편없어진다. 따라서 이러한 경우를 피하면서 아이스크림을 3가지 선택하려고 한다. 이때 선택하는 방법이 몇 가지인지 구하려고 한다.

입력
첫째 줄에 정수 N과 M이 주어진다. N은 아이스크림 종류의 수이고, M은 섞어먹으면 안 되는 조합의 개수이다. 아래 M개의 줄에는 섞어먹으면 안 되는 조합의 번호가 주어진다. 같은 조합은 두 번 이상 나오지 않는다. (1 ≤ N ≤ 200, 0 ≤ M ≤ 10,000)

출력
첫째 줄에 가능한 방법이 총 몇 개 있는지 출력한다.
'''

from sys import stdin
input = stdin.readline

def getCombi(arr, n):
  res = []
  if n == 0:
    return [[]]
  for i in range(len(arr)-n+1):
    for combi in getCombi(arr[i+1:], n-1):
      res.append([arr[i]]+combi)
  return res

n, m = map(int, input().split())
a = [i for i in range(1, n+1)]
badcombi = []
for _ in range(m):
  x, y = map(int, input().split())
  badcombi.append({x, y})

isOk = True
cnt = 0
for li in getCombi(a, 3):
  isOk = True
  # print(li, end=':')
  for badli in badcombi:
    # print(len(set(li)-badli), end=' ')
    if len(set(li)-badli) <= 1:
      isOk = False
      break
  if isOk:
    cnt += 1
  # print()

print(cnt)
