'''
블로그를 시작한 지 N일이 지났다. X일 동안 가장 많이 들어온 방문자 수와 기간이 몇 개 있는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 블로그를 시작하고 지난 일수 N과 X가 공백으로 구분되어 주어진다. (1 ≤ X ≤ N ≤ 250,000)
둘째 줄에는 블로그 시작 1일차부터 N일차까지 하루 방문자 수가 공백으로 구분되어 주어진다. (하루 방문자 수는 최대 8,000이다.)

출력
첫째 줄에 X일 동안 가장 많이 들어온 방문자 수를 출력한다. 만약 최대 방문자 수가 0명이라면 SAD를 출력한다.
만약 최대 방문자 수가 0명이 아닌 경우 둘째 줄에 기간이 몇 개 있는지 출력한다.
'''

n, x = map(int, input().split())
a = list(map(int, input().split()))

curSum = sum(a[0:x])
maxSum = curSum
cntMax = 1
for i in range(1, n-x+1):
  curSum = curSum-a[i-1]+a[i+x-1]
  if curSum > maxSum:
    maxSum = curSum
    cntMax = 1
  elif curSum == maxSum:
    cntMax += 1

if maxSum == 0:
  print("SAD")
else:
  print(maxSum)
  print(cntMax)
