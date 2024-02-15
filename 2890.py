'''
문제
카약 대회를 개최했다. 위성 사진을 바탕으로 실시간 순위를 계산하는 프로그램을 만들려고 한다.

위성 사진은 R행 C열이다. 모든 줄의 첫 번째 글자는 'S'이고 출발선을 의미한다. 또, 마지막 글자는 'F'이고 이것은 결승선을 의미한다. 대회에 참가한 팀은 총 9팀이고, 각 팀은 1부터 9까지 번호가 매겨져 있다. 카약은 항상 열에 대해 연속하는 세 칸을 차지하며, 카약 번호로 표시한다. 마지막으로 물은 '.'로 나타나 있다.

팀의 순위는 결승선으로부터 떨어진 거리로 측정한다. 가까울수록 순위가 높다. 만약, 두 팀이 결승선과 떨어진 거리가 같다면, 같은 등수이다.

입력
첫째 줄에 R과 C가 주어진다. 다음 R개 줄에는 '.', 'S', 'F', '1'~'9'로 이루어진 위성 지도가 주어진다. 한 줄에는 최대 한 개의 카약만 있고, 위성 사진에 있는 카약은 항상 9개이다. (10 ≤ R, C ≤ 50)

출력
출력은 총 9줄을 해야 한다. i번째 줄에는 i번 팀의 등수를 출력한다. (i=1~9)
'''

boat = ['111', '222', '333', '444', '555', '666', '777', '888', '999']

def findBoatPos(str):
    position = -1
    boatLabel = 0
    for i in range(9):
        val = str.find(boat[i])
        if val != -1:
            position = val
            boatLabel = boat[i]
            break    
    return (boatLabel, position)

R, C = map(int, input().split())

currentCapture = list()

for i in range(R):
    boatLabel, position = findBoatPos(input())
    if position != -1:
        currentCapture.append([boatLabel, position])

currentCapture.sort(key = lambda x:x[1], reverse = True)
#print(currentCapture)

result = list()
rank = 1
result.append([currentCapture[0][0], rank])

for i in range(1,9):
    if currentCapture[i][1] == currentCapture[i-1][1]:
        result.append([currentCapture[i][0], rank])
    else:
        rank += 1
        result.append([currentCapture[i][0], rank])

result.sort(key = lambda x:x[0])
#print(result)

for ent in result:
    print(ent[1])