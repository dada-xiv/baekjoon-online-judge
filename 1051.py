'''
문제
N×M크기의 직사각형이 있다. 각 칸에는 한 자리 숫자가 적혀 있다. 이 직사각형에서 꼭짓점에 쓰여 있는 수가 모두 같은 가장 큰 정사각형을 찾는 프로그램을 작성하시오. 이때, 정사각형은 행 또는 열에 평행해야 한다.

입력
첫째 줄에 N과 M이 주어진다. N과 M은 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 수가 주어진다.

출력
첫째 줄에 정답 정사각형의 크기를 출력한다.
'''

n, m = map(int, input().split())
a = list()
maxWidth = 1

for _ in range(n):
  a.append(list(map(int, input())))

for w in range(2, min(n, m)+1):
  # print(w)
  for i in range(0, n-w+1):
    for j in range(0, m-w+1):
      # print(a[i][j], a[i][j+w-1], a[i+w-1][j], a[i+w-1][j+w-1])
      if a[i][j] == a[i][j+w-1] == a[i+w-1][j] == a[i+w-1][j+w-1]:
        if w > maxWidth:
          maxWidth = w

print(maxWidth**2)
