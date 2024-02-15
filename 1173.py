'''
문제
운동을 하는 과정은 1분 단위로 나누어져 있다. 매 분마다 운동과 휴식 중 하나를 선택해야 한다.

운동을 선택한 경우, 맥박이 T만큼 증가한다. 즉, 맥박이 X였다면, 1분 동안 운동을 한 후 맥박이 X+T가 되는 것이다. 맥박이 M을 넘는 것을 원하지 않기 때문에, X+T가 M보다 작거나 같을 때만 운동을 할 수 있다. 휴식을 선택하는 경우 맥박이 R만큼 감소한다. 즉, 맥박이 X였다면, 1분 동안 휴식을 한 후 맥박은 X-R이 된다. 맥박은 m보다 낮아지면 안된다. 

따라서, X-R이 m보다 작으면 맥박은 m이 된다.

초기 맥박은 m이다. 운동을 N분 하려고 한다. 이때 운동을 N분하는데 필요한 시간의 최솟값을 구해보자. 운동하는 시간은 연속되지 않아도 된다.

입력
첫째 줄에 다섯 정수 N, m, M, T, R이 주어진다.

출력
첫째 줄에 운동을 N분하는데 필요한 시간의 최솟값을 출력한다. 만약 운동을 N분 할 수 없다면 -1을 출력한다.

제한
1 ≤ N, T, R ≤ 200
50 ≤ m ≤ M ≤ 200
'''
# 5 70 120 25 15
# 100 50 100 5 200

# import math
#  minRest = math.floor(minRest)

N, m, M, T, R = map(int, input().split())
beat = m
trainingTime = 0
restTime = 0

if beat+T > M:
  print("-1")
else:
  while trainingTime < N:
    if beat + T <= M:
      beat += T
      trainingTime += 1
    else:
      beat -= R
      if beat < m:
        beat = m
      restTime += 1
    # print(f"{restTime}:{trainingTime}, {beat}")
  print(restTime+trainingTime)
