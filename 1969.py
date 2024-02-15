'''
문제
DNA는 서로 다른 4가지의 뉴클레오티드로 이루어져 있다(A,T,G,C) Hamming Distance란 길이가 같은 두 DNA가 있을 때, 각 위치의 뉴클오티드 문자가 다른 것의 개수이다. “AGCAT"와 ”GGAAT"는 첫 번째 글자와 세 번째 글자가 다르므로 Hamming Distance는 2이다.

N개의 길이 M인 DNA s1, s2, ..., sn가 주어져 있을 때 Hamming Distance의 합이 가장 작은 DNA s를 구하는 프로그램을 작성하시오. 즉, s와 s1의 Hamming Distance + s와 s2의 Hamming Distance + s와 s3의 Hamming Distance ... 의 합이 최소가 된다는 의미이다.

입력
첫 줄에 DNA의 수 N과 문자열의 길이 M이 주어진다. 그리고 둘째 줄부터 N+1번째 줄까지 N개의 DNA가 주어진다. N은 1,000보다 작거나 같은 자연수이고, M은 50보다 작거나 같은 자연수이다.

출력
첫째 줄에 Hamming Distance의 합이 가장 작은 DNA 를 출력하고, 둘째 줄에는 그 Hamming Distance의 합을 출력하시오. 그러한 DNA가 여러 개 있을 때에는 사전순으로 가장 앞서는 것을 출력한다.
'''

N, M = map(int, input().split())
seq = list()
for _ in range(N):
  seq.append(list(map(str, input())))

theDNA = list()
nucl = ['A', 'C', 'G', 'T']

for j in range(M):
  net = {'A':0, 'C':0, 'G':0, 'T':0}
  for i in range(N):
    net[seq[i][j]]+=1
  max = net[nucl[0]]
  maxNucl = nucl[0]
  for i in range(1, 4):
    if net[nucl[i]]>max:
      max = net[nucl[i]]
      maxNucl = nucl[i]
  theDNA.append(maxNucl)

print(''.join(theDNA))

diffsum = 0
for i in range(N):
  diffsum += sum(1 for a, b in zip(theDNA, seq[i]) if a != b)
print(diffsum)