'''
문제
Given an array of integer numbers with 5 elements and for each of its elements, find the smallest prime number which is not less than that element.

입력
The first line shows the number of test cases (T).

For each test case, we will have an array of integers (I) with length n in space-separated format.

0 < I < 106
0 < n < 106
출력
Print the sum of obtained prime numbers for each test case.
'''


N = 107
primes = [True for _ in range(N+1)]
for i in range(2, int((N)**0.5)+1):
  if primes[i]:
    for k in range(i+i, N+1, i):
      primes[k] = False

n = int(input())

prev=2
for i in range(3, N+1):
  if primes[i]:
    if (prev*i>n):
      # print(prev, i, prev*i)
      print(prev*i)
      break
    prev=i
