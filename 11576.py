'''
A진법으로 나타낸 숫자를 B진법으로 변환시켜주는 프로그램을 작성하시오.

입력
입력의 첫 줄에는 진법 A와 진법 B가 공백을 구분으로 주어진다. A와 B는 모두 2이상 30이하의 자연수다. 입력의 두 번째 줄에는 A진법으로 나타낸 숫자의 자리수의 개수 m(1 ≤ m ≤ 25)이 주어진다. 세 번째 줄에는 A진법을 이루고 있는 숫자 m개가 공백을 구분으로 높은 자릿수부터 차례대로 주어진다. 각 숫자는 0이상 A미만임이 보장된다. 또한 수가 0으로 시작하는 경우는 존재하지 않는다. A진법으로 나타낸 수를 10진법으로 변환하였을 때의 값은 양의 정수이며 2^{20}보다 작다.

출력
입력으로 주어진 A진법으로 나타낸 수를 B진법으로 변환하여 출력한다.
'''


def decToB(n, m):
  q = -1
  res = list()
  while q != 0:
    q = n//m
    r = n % m
    # print(q, r)
    res.append(r)
    n = q
  res.reverse()
  return res

a, b = map(int, input().split())
lenA = int(input())
dA = list(map(int, input().split()))
numA = 0
for i in range(lenA):
  numA += dA[lenA-i-1]*(a**i)
# print(numA)
# print(decToB(numA, b))
print(" ".join(map(str, decToB(numA, b))))
