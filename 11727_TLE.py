'''
문제
2×n 직사각형을 1×2, 2×1과 2×2 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)

출력
첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.
'''

'''
타일 종류 |, =, ㅁ 3가지

n=짝수:
= or ㅁ타일은 0개 ~ 최대 n/2개 있을 수 있다

n=홀수: 
= or ㅁ타일은 0개 ~ 최대 (n-1)/2개 있을 수 있다
'''

import math
n = int(input())
if n % 2 == 0:
  maxV = int(n/2)
else:
  maxV = int((n-1)/2)
sum = 0

for k1 in range(maxV+1):
  for k2 in range(maxV-k1+1):
    r = n-2*(k1+k2)
    sum += math.factorial(r+k1+k2)//(math.factorial(k1)* math.factorial(k2)*math.factorial(r))

print(sum % 10007)
