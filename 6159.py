'''
문제
Farmer is taking the cows to a costume party, but he only has one costume. The costume fits precisely two cows with a length of S (1 <= S <= 1,000,000). Farmer has N cows (2 <= N <= 20,000) conveniently numbered 1..N; cow i has length L_i (1 <= L_i <= 1,000,000). Two cows can fit into the costume if the sum of their lengths is no greater than the length of the costume. Farmer wants to know how many pairs of two distinct cows will fit into the costume.

입력
Line 1: Two space-separated integers: N and S
Lines 2..N+1: Line i+1 contains a single integer: L_i
출력
Line 1: A single integer representing the number of pairs of cows farmer can choose. Note that the order of the two cows does not matter.
'''

from sys import stdin
input = stdin.readline
n, s = map(int, input().split())
ar = list()
for _ in range(n):
  ar.append(int(input()))
ar.sort()
# print(ar)
idxL, idxR = 0, n-1
cnt = 0
while idxL < idxR:
  # print(idxL+1, idxR+1, cnt)
  sumP = ar[idxL]+ar[idxR]
  if sumP > s:
    idxR -= 1
  else:
    # print(f"found: {ar[idxL]}+{ar[idxR]}={sumP}")
    cnt += idxR-idxL
    idxL += 1
print(cnt)
