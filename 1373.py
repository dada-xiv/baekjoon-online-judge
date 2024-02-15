'''
문제
2진수가 주어졌을 때, 8진수로 변환하는 프로그램을 작성하시오.

입력
첫째 줄에 2진수가 주어진다. 주어지는 수의 길이는 1,000,000을 넘지 않는다.

출력
첫째 줄에 주어진 수를 8진수로 변환하여 출력한다.
'''

from sys import stdin
input = stdin.readline
numBin = input().rstrip()
lenBin = len(numBin)

if len(numBin) % 3 != 0:
  lenZero = 3*(lenBin//3+1)-lenBin
  numBin = "0"*lenZero + numBin
  lenBin = lenZero + lenBin

# print(numBin, lenBin)
# print(lenBin//3)
res = ""
for i in range(lenBin//3):
  s = numBin[i*3:i*3+3]
  # print(s[0], s[1], s[2])
  res += str(int(s[0])*4+int(s[1])*2+int(s[2]))

print(res)
