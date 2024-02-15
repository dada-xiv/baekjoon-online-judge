'''
문제
높이만 다르고 모양이 같은 막대기를 일렬로 세운 후, 왼쪽부터 차례로 번호를 붙인다. 이를테면 막대기의 높이가 순서대로 6, 9, 7, 6, 4, 6 이면 오른쪽에서 보면 3개(6번, 3번, 2번)의 막대기가 보인다.

N개의 막대기에 대한 높이 정보가 주어질 때, 오른쪽에서 보아서 몇 개가 보이는지를 알아내는 프로그램을 작성하려고 한다.

입력
첫 번째 줄에는 막대기의 개수를 나타내는 정수 N (2 ≤ N ≤ 100,000)이 주어지고 이어지는 N줄 각각에는 막대기의 높이를 나타내는 정수 h(1 ≤ h ≤ 100,000)가 주어진다.

출력
오른쪽에서 N개의 막대기를 보았을 때, 보이는 막대기의 개수를 출력한다.
'''

from sys import stdin
input = stdin.readline
N = int(input())
a = list()

for _ in range(N):
  a.append(int(input()))

max = a[-1]
cnt = 1

for i in reversed(range(N)):
  if a[i] > max:
    max = a[i]
    cnt += 1

print(cnt)
