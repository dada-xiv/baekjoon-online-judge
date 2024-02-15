'''
문제
nCm을 출력한다.

입력
n과 m이 주어진다. (5 ≤ n ≤ 100, 5 ≤ m ≤ 100, m ≤ n)

출력
nCm을 출력한다.
'''

from math import comb
n, m = map(int, input().split())
print(comb(n, m))
