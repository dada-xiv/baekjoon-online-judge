'''
문제
한 변이 1인 정사각형부터 시작하여 앵무조개의 나선 모양처럼 점점 큰 정사각형을 붙여서 직사각형을 이루도록 한다. 도형을 구성하는 정사각형 타일 한 변의 길이를 안쪽 타일부터 시작하여 차례로 적으면 다음과 같다.

1, 1, 2, 3, 5, 8, ... 

타일의 개수 N(1 ≤ N ≤ 80)이 주어졌을 때, N개의 타일로 구성된 직사각형의 둘레를 구하는 프로그램을 작성하시오.

예를 들어, 처음 다섯개의 타일이 구성하는 직사각형(위에서 빨간색으로 표시한 직사각형)의 둘레는 26이다.

입력
타일의 개수를 나타내는 정수 N(1 ≤ N ≤ 80)이 주어진다.

출력
N개의 타일이 구성하는 타일 장식물 직사각형의 둘레를 출력한다. 
'''

n = int(input())
d = [(0, 0), (1, 4)]
for i in range(2, n+1):
  w = d[i-2][0]+d[i-1][0]
  l = d[i-1][1]-w+3*w
  d.append((w, l))
print(d[-1][1])
