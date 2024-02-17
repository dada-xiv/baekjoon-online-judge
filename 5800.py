'''
문제
각 반의 학생들의 성적이 주어졌을 때, 최대 점수, 최소 점수, 점수 차이를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 반의 수 K (1 ≤ K ≤ 100)가 주어진다. 다음 K개 줄에는 각 반의 학생수 N (2 ≤ N ≤ 50)과 각 학생의 성적이 주어진다. 시험 성적은 0보다 크거나 같고, 100보다 작거나 같은 정수이고, 공백으로 나누어져 있다. 

출력
각 반에 대한 출력은 다음과 같이 두 줄로 이루어져 있다.
첫째 줄에는 "Class X"를 출력한다. X는 반의 번호이며 입력으로 주어진 순서대로 1부터 증가한다.
둘째 줄에는 가장 높은 점수, 낮은 점수, 성적을 내림차순으로 정렬했을 때 가장 큰 인접한 점수 차이를 다음 형식으로 출력한다.
Class 1
Max 78, Min 23, Largest gap 46
'''

k = int(input())
for j in range(k):
  arr = list(map(int, input().split()))
  n = arr[0]
  a = arr[1:]
  a.sort()
  min = a[0]
  max = a[n-1]
  gap = a[1]-a[0]
  for i in range(2, n):
    gapc = a[i]-a[i-1]
    if gapc > gap:
      gap = gapc
  print(f"Class {j+1}")
  print(f"Max {max}, Min {min}, Largest gap {gap}")