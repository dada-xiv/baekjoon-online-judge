'''
문제
돈을 똑같이 분배하고자 한다.
한 명에게 얼마씩 돈을 줄 수 있는가?
동일하게 분배한 후 남는 돈은 얼마인가?

입력
첫째 줄에는 가진 돈 n과 돈을 받으러 온 사람의 수 m이 주어진다. (1 ≤ m ≤ n ≤ 101000, m과 n은 10진수 정수)

출력
첫째 줄에 한 명 돌아가는 돈의 양을 출력한다. 그리고 두 번째 줄에는 1원씩 분배할 수 없는 남는 돈을 출력한다.
'''

from sys import stdin
input = stdin.readline
n, m = map(int, input().split())
q = n//m
print(q)
print(n-m*q)

