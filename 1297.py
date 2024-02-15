'''
문제
인터넷 쇼핑몰 관리자에게 이메일을 보내서 실제 높이와 실제 너비를 보내달라고 했지만, 관리자는 실제 높이와 실제 너비를 보내지 않고 그것의 비율을 보내왔다. TV의 대각선 길이와, 높이 너비의 비율이 주어졌을 때, 실제 높이와 너비의 길이를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 TV의 대각선 길이 D, TV의 높이 비율 H, TV의 너비 비율 W이 공백 한 칸을 사이에 두고 주어진다.

출력
첫째 줄에 TV의 높이와 TV의 너비를 공백 한 칸을 이용해서 구분지은 후 출력한다. 만약, 실제 TV의 높이나 너비가 소수점이 나올 경우에는 그 수보다 작으면서 가장 큰 정수로 출력한다. (예) 1.7 -> 1

제한
5 ≤ D ≤ 1,000
1 ≤ H ≤ 99
2 ≤ W ≤ 100
H < W
D, H, W는 정수
'''

import math
from sys import stdin
input = stdin.readline
D, H, W = map(int, input().split())
a = math.sqrt(D**2/(W**2+H**2))
width = int(a*W)
height = int(a*H)
print(height, width)