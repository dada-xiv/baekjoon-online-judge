from collections import deque

a = [0 for i in range(5)]
print(a)

'''
입력이 여러 줄 있을 때:

import sys
input = sys.stdin.readline
for s in sys.stdin:
  print(s.rstrip())
'''

# list 등 인덱스 범위 맞추기
idxLen = 6
def getIdx(n):
  if n < 0:
    n += idxLen
  elif n >= idxLen:
    n -= idxLen
  return n

# Round-off vs Round-to-nearest-even
def roundT(val, digits):
  return round(val+10**(-len(str(val))-1), digits)

# 무언가 에러가 남
import math
from fractions import Fraction
n, m = 6, 5
print(Fraction(math.factorial(n)/(math.factorial(m)*math.factorial(n-m))))

# 에러 없음
from math import comb
print(comb(n, m))