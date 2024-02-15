'''
문제
2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. (-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.

출력
첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.
'''

def merge(a, left, mid, right):
    pivotL = left
    pivotR = mid + 1
    k = left
    sorted = [0]*(right-left+1)

    while pivotL<=mid and pivotR<=right:
        if a[pivotL][0] < a[pivotR][0] or (a[pivotL][0] == a[pivotR][0] and a[pivotL][1] < a[pivotR][1]):
            sorted[k-left] = a[pivotL]
            k += 1
            pivotL += 1
        else:
            sorted[k-left] = a[pivotR]
            k += 1
            pivotR += 1

    while pivotL <= mid:
        sorted[k-left] = a[pivotL]
        k += 1
        pivotL += 1

    while pivotR <= right:
        sorted[k-left] = a[pivotR]
        k += 1
        pivotR += 1

    for i in range(left, right+1):
        a[i] = sorted[i-left]

def mergeSort(a, left, right):
    if left < right:
        mid = (left + right) // 2
        mergeSort(a, left, mid)
        mergeSort(a, mid+1, right)
        merge(a, left, mid, right)


a = list()
N = int(input()) # len(a)
for i in range(N):
    x, y = map(int, input().split())
    a.append([x,y])

mergeSort(a, 0, N-1)
for sublist in a:
    print(sublist[0], sublist[1])
