'''
문제
종이는 가로방향과 세로 방향으로 1㎝마다 점선이 그어져 있다. 점선을 따라 종이를 자르려고 한다. 가로 점선을 따라 자르는 경우는 종이의 왼쪽 끝에서 오른쪽 끝까지, 세로 점선인 경우는 위쪽 끝에서 아래쪽 끝까지 한 번에 자른다. 예를 들어, 가로 길이 10㎝이고 세로 길이 8㎝인 종이를 3번 가로 점선, 4번 세로 점선, 그리고 2번 가로 점선을 따라 자르면 여러 개의 종이 조각으로 나뉘게 된다. 이때 가장 큰 종이 조각의 넓이는 30㎠이다.

입력으로 종이의 가로 세로 길이, 그리고 잘라야할 점선들이 주어질 때, 가장 큰 종이 조각의 넓이가 몇 ㎠인지를 구하는 프로그램을 작성하시오.

입력
첫줄에는 종이의 가로와 세로의 길이가 차례로 자연수로 주어진다. 가로와 세로의 길이는 최대 100㎝이다. 둘째 줄에는 칼로 잘라야하는 점선의 개수가 주어진다. 셋째 줄부터 마지막 줄까지 한 줄에 점선이 하나씩 아래와 같은 방법으로 입력된다. 가로로 자르는 점선은 0과 점선 번호가 차례로 주어지고, 세로로 자르는 점선은 1과 점선 번호가 주어진다. 입력되는 두 숫자 사이에는 빈 칸이 하나씩 있다.

출력
첫째 줄에 가장 큰 종이 조각의 넓이를 출력한다. 단, 넓이의 단위는 출력하지 않는다.
'''

w, h = map(int, input().split())
n = int(input())
warr = [0]
harr = [0]
for _ in range(n):
  ix, val = map(int, input().split())
  if ix == 0:
    harr.append(val)
  elif ix == 1:
    warr.append(val)
warr.sort()
warr.append(w)
harr.sort()
harr.append(h)
# print(warr, harr)
hd = list()
for i in range(1, len(harr)):
  hd.append(harr[i]-harr[i-1])
wd = list()
for j in range(1, len(warr)):
  wd.append(warr[j]-warr[j-1])
print(max(hd)*max(wd))
