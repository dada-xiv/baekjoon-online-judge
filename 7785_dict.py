'''
문제
각 직원은 자기가 원할 때 출근할 수 있고, 아무때나 퇴근할 수 있다. 출입카드 시스템의 로그는 어떤 사람이 회사에 들어왔는지, 나갔는지가 기록되어져 있다. 로그가 주어졌을 때, 현재 회사에 있는 모든 사람을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 로그에 기록된 출입 기록의 수 n이 주어진다. (2 ≤ n ≤ 10^6) 다음 n개의 줄에는 출입 기록이 순서대로 주어지며, 각 사람의 이름이 주어지고 "enter"나 "leave"가 주어진다. "enter"인 경우는 출근, "leave"인 경우는 퇴근이다.

회사에는 동명이인이 없으며, 대소문자가 다른 경우에는 다른 이름이다. 사람들의 이름은 알파벳 대소문자로 구성된 5글자 이하의 문자열이다.

출력
현재 회사에 있는 사람의 이름을 사전 순의 역순으로 한 줄에 한 명씩 출력한다.
'''

import sys
input = sys.stdin.readline

n = int(input())
a = dict() # Dictionary
for _ in range(n):
    name, status = input().split()
    if status == 'enter':
        a[name] = True
    elif status == 'leave':
        a[name] = False

a_sorted = sorted(a.items(), reverse=True)
for name, isTrue in a_sorted:
    if isTrue == True:
        print(name)
