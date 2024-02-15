'''
문제
총 N개의 문자열로 이루어진 집합 S가 주어진다. 입력으로 주어지는 M개의 문자열 중에서 집합 S에 포함되어 있는 것이 총 몇 개인지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 문자열의 개수 N과 M (1 ≤ N ≤ 10,000, 1 ≤ M ≤ 10,000)이 주어진다. 다음 N개의 줄에는 집합 S에 포함되어 있는 문자열들이 주어진다. 다음 M개의 줄에는 검사해야 하는 문자열들이 주어진다.

입력으로 주어지는 문자열은 알파벳 소문자로만 이루어져 있으며, 길이는 500을 넘지 않는다. 집합 S에 같은 문자열이 여러 번 주어지는 경우는 없다.

출력
첫째 줄에 M개의 문자열 중에 총 몇 개가 집합 S에 포함되어 있는지 출력한다.

cf) 파이썬에서는 set 또는 dictionary가 list보다 빠르다. 왜냐하면 set 또는 dictionary는 단어를 숫자로 mapping하고 이 숫자를 인덱스처럼 활용하는 hash table을 활용하기 때문이다. 
'''

N, M = map(int, input().split())

s = {} #dictionary
for i in range(N):
    tmp = input()
    s[tmp] = True

total = 0
for _ in range(M):
    ent = input()
    if ent in s:
        total += 1

print(total)