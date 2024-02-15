'''
두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)
첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.
'''
A, B = map(int, input().split())
print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)
