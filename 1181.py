'''
문제
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

길이가 짧은 것부터
길이가 같으면 사전 순으로
단, 중복된 단어는 하나만 남기고 제거해야 한다.

입력
첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 주어지는 문자열의 길이는 50을 넘지 않는다.

출력
조건에 따라 정렬하여 단어들을 출력한다.
'''

def merge(a, left, mid, right):
    pivotL = left
    pivotR = mid + 1
    k = left
    sorted = [0]*(right-left+1)

    while pivotL<=mid and pivotR<=right:
        if len(a[pivotL]) < len(a[pivotR]) or (len(a[pivotL]) == len(a[pivotR]) and a[pivotL] < a[pivotR]):
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
    x = input()
    a.append(x)

mergeSort(a, 0, N-1)

for i in range(N-1):
    if a[i]!=a[i+1]:
        print(a[i])
print(a[N-1])
