'''
문제
길이가 N으로 같은 문자열 X와 Y가 있을 때, 두 문자열 X와 Y의 차이는 X[i] ≠ Y[i]인 i의 개수이다. 예를 들어, X=”jimin”, Y=”minji”이면, 둘의 차이는 4이다.

두 문자열 A와 B가 주어진다. 이때, A의 길이는 B의 길이보다 작거나 같다. 이제 A의 길이가 B의 길이와 같아질 때 까지 다음과 같은 연산을 할 수 있다.

1. A의 앞에 아무 알파벳이나 추가한다.
2. A의 뒤에 아무 알파벳이나 추가한다.
이때, A와 B의 길이가 같으면서, A와 B의 차이를 최소로 하는 프로그램을 작성하시오.

입력
첫째 줄에 A와 B가 주어진다. A와 B의 길이는 최대 50이고, A의 길이는 B의 길이보다 작거나 같고, 알파벳 소문자로만 이루어져 있다.

출력
A와 B의 길이가 같으면서, A와 B의 차이를 최소가 되도록 할 때, 그 차이를 출력하시오.
'''


def getDiffNum(stA, stB, n):
  cnt = 0
  for i in range(n):
    if stA[i] != stB[i]:
      cnt += 1
  return cnt


strA, strB = map(str, input().split())
lenA = len(strA)
lenB = len(strB)
lendiff = lenB-lenA
min = lenB
for k in range(lendiff+1):
  # print(k, lendiff-k, end=" : ")
  strAa = strB[:k]+strA+strB[lenB-lendiff+k:]
  # print(strAa)
  diffAB = getDiffNum(strAa, strB, lenB)
  if diffAB < min:
    min = diffAB

print(min)
