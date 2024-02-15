'''
문제
N명이 참가하는 토너먼트는 다음과 같이 진행된다: N명의 참가자는 1번부터 N번까지 배정받는다. 그리고 서로 인접한 번호끼리 대결을 한다. 이긴 사람은 다음 라운드에 진출하고, 진 사람은 그 라운드에서 떨어진다. 만약 라운드의 참가자가 홀수명이라면, 마지막 번호를 가진 참가자는 다음 라운드로 자동 진출한다. 다음 라운드에선 다시 참가자의 번호를 1번부터 매긴다. 이때, 번호를 매기는 순서는 처음 번호의 순서를 유지하면서 1번부터 매긴다. 즉 1번과 2번이 대결을 해서 1번이 진출하고, 3번과 4번이 대결을 해서 4번이 진출했다면, 4번은 다음 라운드에서 번호 2번을 배정받는다. 번호를 다시 배정받은 후에 한 명만 남을 때까지 라운드를 계속 한다.

A는 B와 대결하는지 궁금해졌다. 일단 A와 B는 서로 대결하기 전까지 항상 이긴다고 가정한다. 1라운드에서 A의 번호와 B의 번호가 주어질 때, 과연 A와 B가 몇 라운드에서 대결하는지 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 참가자의 수 N과 1 라운드에서 A의 번호와 B의 번호가 순서대로 주어진다. N은 2보다 크거나 같고, 100,000보다 작거나 같은 자연수이고, A의 번호와 B의 번호는 N보다 작거나 같은 자연수이고, 서로 다르다.

출력
첫째 줄에 A와 B가 대결하는 라운드 번호를 출력한다. 만약 서로 대결하지 않을 때는 -1을 출력한다.
'''

import math

def defLR(P, Li, Le, Ri, Re):
  if P >= Li and P <= Le:
    return 'L'
  elif P >= Ri and P <= Re:
    return 'R'

N, A, B = map(int, input().split())
n = math.ceil(math.log2(N))

flgA, flgB = '', ''
Li, Le, Ri, Re = 1, 2**(n-1), 2**(n-1)+1, 2**n

k = n
while k > 0:
  # print('k =', k)
  # print(Li, Le, Ri, Re)
  flgA = defLR(A, Li, Le, Ri, Re)
  flgB = defLR(B, Li, Le, Ri, Re)
  # print(flgA, flgB)
  if flgA == 'L' and flgB == 'L':
    Li, Le, Ri, Re = Li, int((Le-Li+1)/2)+Li-1, int((Le-Li+1)/2)+Li, Le
    1, 2**(k-2), 2**(k-2)+1, 2**(k-1)
  elif flgA == 'R' and flgB == 'R':
    Li, Le, Ri, Re = Ri, int((Re-Ri+1)/2)+Ri-1, int((Re-Ri+1)/2)+Ri, Re
  elif flgA == 'L' and flgB == 'R':
    print(k)
    break
  k -= 1

