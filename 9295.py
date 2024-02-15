'''
입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다.

각 테스트 케이스는 한 줄로 이루어져 있으며, 주사위를 두 번 던져 나온 두 수를 입력한다.

출력
각 테스트 케이스마다 "Case x: "를 출력한 다음, 주사위를 두 번 던져 나온 두 수의 합을 출력한다. 테스트 케이스 번호(x)는 1부터 시작한다.
'''

def printFibonacci(n):
    a=0
    b=1

    if n==0:
        return a
    elif n==1:
        return b
    else:
        for i in range(2,n):
            c = a + b
            a = b
            b = c
        return a+b

n = int(input())

print(printFibonacci(n))
