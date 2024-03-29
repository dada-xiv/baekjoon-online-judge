'''
문제
하루 동안 팔린 책의 제목이 입력으로 들어왔을 때, 가장 많이 팔린 책의 제목을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 오늘 하루 동안 팔린 책의 개수 N이 주어진다. 이 값은 1,000보다 작거나 같은 자연수이다. 둘째부터 N개의 줄에 책의 제목이 입력으로 들어온다. 책의 제목의 길이는 50보다 작거나 같고, 알파벳 소문자로만 이루어져 있다.

출력
첫째 줄에 가장 많이 팔린 책의 제목을 출력한다. 만약 가장 많이 팔린 책이 여러 개일 경우에는 사전 순으로 가장 앞서는 제목을 출력한다.
'''

from sys import stdin
input = stdin.readline

N = int(input())
data = dict()
max = 0
for _ in range(N):
  val = input().rstrip()
  if val not in data:
    data[val] = 1
  else:
    data[val] += 1
  if data[val] > max:
    max = data[val]

res=[]
for k, v in data.items():
  if v==max:
    res.append(k)
res.sort()
print(res[0])