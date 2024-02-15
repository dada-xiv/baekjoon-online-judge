'''
문제
타일은 '1'과 '00' 두 가지가 있다. 이 타일로 길이가 N인 2진수를 만들려고 한다.

N=1: 1 (1가지)
N=2: 00, 11 (2가지)
N=3: 100, 111, 001 (3가지)
N=4: 0011, 0000, 1001, 1100, 1111 (5가지)

N이 주어졌을 때 만들 수 있는 2진수의 가짓수를 구하시오.

입력
첫 번째 줄에 자연수 N이 주어진다. (1 ≤ N ≤ 1,000,000)

출력
첫 번째 줄에 만들 수 있는 길이가 N인 모든 2진 수열의 개수를 15746으로 나눈 나머지를 출력한다.
'''


def getTileNum(n):
  m = 15746
  f1 = 1
  f2 = 2
  if n == 1:
    return f1
  elif n == 2:
    return f2
  else:
    for i in range(3, n):
      f3 = (f1 + f2) % m
      f1 = f2
      f2 = f3
    return (f1 + f2) % m

n = int(input())
print(getTileNum(n))
