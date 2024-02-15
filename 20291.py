'''
문제
파일을 확장자 별로 정리해서 확장자들을 사전 순으로 정렬해주는 프로그램을 작성하시오.

입력
첫째 줄에 바탕화면에 있는 파일의 개수 N(1 ≤ N ≤ 50,000)이 주어진다.

둘째 줄부터 N개 줄에 바탕화면에 있는 파일의 이름이 주어진다. 파일의 이름은 알파벳 소문자와 점(.)으로만 구성되어 있다. 점은 정확히 한 번 등장하며, 파일 이름의 첫 글자 또는 마지막 글자로 오지 않는다. 각 파일의 이름의 길이는 최소 3, 최대 100이다.

출력
확장자의 이름과 그 확장자 파일의 개수를 한 줄에 하나씩 출력한다. 확장자가 여러 개 있는 경우 확장자 이름의 사전순으로 출력한다.
'''

from sys import stdin
input = stdin.readline
n = int(input())
ds = dict()
for _ in range(n):
  ext = input().rstrip().split('.')[1]
  if ext in ds:
    ds[ext] += 1
  else:
    ds[ext] = 1

for k in sorted(ds):
  print(k, ds[k])
