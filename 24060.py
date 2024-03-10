'''
문제
N개의 서로 다른 양의 정수가 저장된 배열 A가 있다. 병합 정렬로 배열 A를 오름차순 정렬할 경우 배열 A에 K 번째 저장되는 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 배열 A의 크기 N(5 ≤ N ≤ 500,000), 저장 횟수 K(1 ≤ K ≤ 108)가 주어진다.
다음 줄에 서로 다른 배열 A의 원소 A1, A2, ..., AN이 주어진다. (1 ≤ Ai ≤ 109)

출력
배열 A에 K 번째 저장 되는 수를 출력한다. 저장 횟수가 K 보다 작으면 -1을 출력한다
'''

n, k = map(int, input().split())
ar = list(map(int, input().split()))
cnt = 0
var = -1

def merge_sort(A, p, r):
  if p < r:
    q = (p + r) // 2
    merge_sort(A, p, q)
    merge_sort(A, q + 1, r)
    merge(A, p, q, r)

def merge(A, p, q, r):
  i, j, t = p, q + 1, 0
  tmp = [0] * (r - p + 1)

  while i <= q and j <= r:
    if A[i] <= A[j]:
      tmp[t] = A[i]
      t += 1
      i += 1
    else:
      tmp[t] = A[j]
      t += 1
      j += 1

  while i <= q:
    tmp[t] = A[i]
    t += 1
    i += 1

  while j <= r:
    tmp[t] = A[j]
    t += 1
    j += 1

  i, t = p, 0
  global cnt,var
  while i <= r:
    A[i] = tmp[t]
    cnt += 1
    if cnt==k:
      var=A[i]
      return
    i += 1
    t += 1

merge_sort(ar, 0, n - 1)
print(var)