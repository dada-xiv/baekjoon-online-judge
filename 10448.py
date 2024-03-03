'''
자연수 n에 대해 n ≥ 1의 삼각수 Tn는 다음과 같이 계산된다.
Tn = 1 + 2 + 3 + ... + n = n(n+1)/2
1796년, 가우스는 모든 자연수가 최대 3개의 삼각수의 합으로 표현될 수 있다고 증명하였다. 예를 들어,
4 = T1 + T2
5 = T1 + T1 + T2
6 = T2 + T2 or 6 = T3
10 = T1 + T2 + T3 or 10 = T4

자연수가 주어졌을 때, 그 정수가 정확히 3개의 삼각수의 합으로 표현될 수 있는지 없는지를 판단해주는 프로그램을 작성하시오. 단 3개의 삼각수가 모두 달라야 할 필요는 없다.

입력
프로그램은 표준입력을 사용한다. 테스트케이스의 개수는 입력의 첫 번째 줄에 주어진다. 각 테스트케이스는 한 줄에 자연수 K (3 ≤ K ≤ 1,000)가 하나씩 포함되어있는 T개의 라인으로 구성되어있다.

출력
프로그램은 표준출력을 사용한다. 각 테스트케이스에 대하여 정확히 한 라인을 출력한다. 만약 K가 정확히 3개의 삼각수의 합으로 표현될수 있다면 1을, 그렇지 않다면 0을 출력한다.
'''

t = list()
lenT = 44
for i in range(1, lenT+1):
  t.append(int(i*(i+1)/2))

def isPossible(num):
  for i in range(lenT):
    for j in range(i, lenT):
      for k in range(j, lenT):
        if t[i]+t[j]+t[k] == num:
          return 1
  return 0

nCase = int(input())
for _ in range(nCase):
  num = int(input())
  print(isPossible(num))
