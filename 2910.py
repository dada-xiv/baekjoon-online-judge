'''
문제
메시지는 숫자 N개로 이루어진 수열이고, 숫자는 모두 C보다 작거나 같다. 이 숫자를 자주 등장하는 빈도순대로 정렬하려고 한다.

만약, 수열의 두 수 X와 Y가 있을 때, X가 Y보다 수열에서 많이 등장하는 경우에는 X가 Y보다 앞에 있어야 한다. 만약, 등장하는 횟수가 같다면, 먼저 나온 것이 앞에 있어야 한다. 이렇게 정렬하는 방법을 빈도 정렬이라고 한다.

수열이 주어졌을 때, 빈도 정렬을 하는 프로그램을 작성하시오.

입력
첫째 줄에 메시지의 길이 N과 C가 주어진다. (1 ≤ N ≤ 1,000, 1 ≤ C ≤ 1,000,000,000)
둘째 줄에 메시지 수열이 주어진다.

출력
첫째 줄에 입력으로 주어진 수열을 빈도 정렬한 다음 출력한다.
'''

from sys import stdin
input = stdin.readline
lenM, c = map(int, input().split())
m = list(map(int, input().split()))
fq = dict()
for i in range(lenM):
  if m[i] in fq:
    fq[m[i]] = (fq[m[i]][0]+1, fq[m[i]][1])
  else:
    fq[m[i]] = (1, i)
fqList = list(zip(fq.keys(), fq.values()))
fqList.sort(key=lambda x: (-x[1][0], x[1][1]))
resList = list()
for a, b in fqList:
  for _ in range(b[0]):
    resList.append(a)
print(' '.join(map(str, resList)))
