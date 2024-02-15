'''
문제
[1]부터 [34]까지의 카드가 무한히 많다. 숫자가 순서대로 주어질 때, 가능한 카드의 배열이 모두 몇 개인지 구하는 프로그램을 작성하시오. 예를들어 27123은 여섯 가지 경우가 있다
[27][1][2][3]
[27][12][3]
[27][1][23]
[2][7][1][2][3]
[2][7][12][3]
[2][7][1][23]

입력
첫 줄에 숫자가 순서대로 주어지며, 이것은 최대 40자 이하의 숫자로 이루어진다.

출력
첫 줄에 가능한 카드 배열이 몇 개인지를 출력한다.
'''

def cntWays(s):
    lenS = len(s)
    if lenS == 0:
        return 1

    count = 0
    for i in range(1, min(3, lenS+1)):
        current = s[:i]
        next = s[i:]
        if (current[0] != '0' and int(current) <= 34):
            count += cntWays(next)

    return count

a = input()
print(cntWays(a))