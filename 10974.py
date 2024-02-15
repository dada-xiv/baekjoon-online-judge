'''
문제
N이 주어졌을 때, 1부터 N까지의 수로 이루어진 순열을 사전순으로 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 8)이 주어진다. 

출력
첫째 줄부터 N!개의 줄에 걸쳐서 모든 순열을 사전순으로 출력한다.
'''

def getPerm(arr, n):
  res = []
  if n==0:
    return [[]]
  for i in range(len(arr)):
    for rest in getPerm(arr[:i]+arr[i+1:],n-1):
      res.append([arr[i]]+rest)
  return res

n = int(input())
a = list()
for i in range(n):
  a.append(i+1)

for li in getPerm(a,n):
  print(" ".join(map(str, li)))