'''
문제
정수 집합 S가 주어졌을때, 다음 조건을 만족하는 구간 [A, B]를 좋은 구간이라고 한다.

- A와 B는 양의 정수이고, A < B를 만족한다.
- A ≤ x ≤ B를 만족하는 모든 정수 x가 집합 S에 속하지 않는다.

집합 S와 n이 주어졌을 때, n을 포함하는 좋은 구간의 개수를 구해보자.

입력
첫째 줄에 집합 S의 크기 L이 주어진다. 둘째 줄에는 집합에 포함된 정수가 주어진다. 셋째 줄에는 n이 주어진다.

출력
첫째 줄에 n을 포함하는 좋은 구간의 개수를 출력한다.

제한
1 ≤ L ≤ 50
집합 S에는 중복되는 정수가 없다.
집합 S에 포함된 모든 정수는 1보다 크거나 같고, 1,000보다 작거나 같다.
1 ≤ n ≤ (집합 S에서 가장 큰 정수)
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

L = int(input())
s = list(map(int, input().split()))
elm = int(input())
s.sort()

sMin = 0
sMax = 0

if L == 1 or s[0] > elm:
  sMin = 1
  sMax = s[0]-1
else:
  for i in range(L):
    if s[i] > elm:
      sMin = s[i-1]+1
      sMax = s[i]-1
      break

# print(sMin, sMax)
arr = []
numGInterval = 0
if sMin > elm or sMax-sMin < 1:
  print(0)
else:
  for i in range(sMin, sMax+1):
    arr.append(i)
  combi = getCombi(arr, 2)
  for item in combi:
    if item[0] <= elm and item[1] >= elm:
      numGInterval += 1
      # print(item)
  print(numGInterval)
