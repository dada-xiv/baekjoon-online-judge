'''
문제
n:m이 주어진다. 두 수를 최대한 약분하여 출력한다.

입력
n과 m이 :을 사이에 두고 주어진다. (1 ≤ n, m ≤ 100,000,000)

출력
두 수를 최대한 약분하여 출력한다.
'''


def gcd(m, n):
  while n:
    m, n = n, m % n
  return m

a, b = map(int, input().split(':'))
g = gcd(a, b)
print(f"{a//g}:{b//g}")
