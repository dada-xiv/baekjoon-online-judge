'''
주어지는 수는 모두 10의 제곱 형태이다. 숫자는 최대 100자리이다. 칠판에 쓰여 있는 문제가 주어졌을 때, 결과를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 양의 정수 A가 주어진다.
둘째 줄에 연산자 + 또는 *가 주어진다.
셋째 줄에 양의 정수 B가 주어진다.
A와 B는 모두 10의 제곱 형태이고, 길이는 최대 100자리이다.

출력
첫째 줄에 결과를 출력한다. 결과는 A+B 또는 A*B이며, 입력에서 주어지는 연산자에 의해 결정된다. 
'''

a = input()
op = input()
b = input()

lenAz = len(a)-1
lenBz = len(b)-1

if op == "*":
    sC = list()
    lenCz = lenAz + lenBz
    for _ in range(lenCz):
        sC.append(0)
    sC.append(1)

elif op == "+":
    sA = list()
    sB = list()

    for _ in range(lenAz):
        sA.append(0)
    sA.append(1)

    for _ in range(lenBz):
        sB.append(0)
    sB.append(1)

    sC = list()
    minC = list()

    lenSA = len(sA)
    lenSB = len(sB)

    if lenSA >= lenSB:
        sC = sA
        for i in range(lenSB):
            sC[i] = sA[i] + sB[i]
    else:
        sC = sB
        for i in range(lenSA):
            sC[i] = sA[i] + sB[i]

lenSC = len(sC)
for i in range(lenSC):
    print(sC[lenSC-i-1], end='')