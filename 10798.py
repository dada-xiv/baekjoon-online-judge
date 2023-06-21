'''
문제
아직 글을 모르는 영석이가 벽에 걸린 칠판에 자석이 붙어있는 글자들을 붙이는 장난감을 가지고 놀고 있다. 아래 그림 1은 영석이가 칠판에 붙여 만든 단어들의 예이다. 
A A B C D D
a f z z 
0 9 1 2 1
a 8 E W g 6
P 5 h 3 k x
그림 1에서 영석이가 세로로 읽은 순서대로 글자들을 공백 없이 출력하면 다음과 같다:
Aa0aPAf985Bz1EhCz2W3D1gkD6x
칠판에 붙여진 단어들이 주어질 때, 영석이가 세로로 읽은 순서대로 글자들을 출력하는 프로그램을 작성하시오.

입력
총 다섯줄의 입력이 주어진다. 각 줄에는 최소 1개, 최대 15개의 글자들이 빈칸 없이 연속으로 주어진다. 주어지는 글자는 영어 대문자 A부터 Z, 영어 소문자 a부터 z, 숫자 0부터 9 중 하나이다. 각 줄의 시작과 마지막에 빈칸은 없다.

출력
영석이가 세로로 읽은 순서대로 글자들을 출력한다. 이때, 글자들을 공백 없이 연속해서 출력한다. 
'''

LINE_LENGTH = 5

a = list()

maxRowLength = 0
for i in range(LINE_LENGTH):
    row = input()
    rowlength = len(row)
    if rowlength > maxRowLength:
        maxRowLength = rowlength
    rowlist = list()
    for c in row:
        rowlist.append(c)
    a.append(rowlist)

for i in range(LINE_LENGTH):
    curRowLength = len(a[i])
    if curRowLength < maxRowLength:
        for j in range(maxRowLength-curRowLength):
            a[i].append('')

for j in range(maxRowLength):
    for i in range(LINE_LENGTH):
        if a[i][j]!='':
            print(a[i][j], end='')



