'''
문제
공식을 이용해 우승할 확률이 가장 높은 팀 이름을 찾으려고 한다. 먼저 다음 4가지 변수의 값을 계산해야 한다.
L = 이름과 팀 이름에서 등장하는 L의 개수
O = 이름과 팀 이름에서 등장하는 O의 개수
V = 이름과 팀 이름에서 등장하는 V의 개수
E = 이름과 팀 이름에서 등장하는 E의 개수
그 다음, 위에서 구한 변수를 다음 식에 입력하면 팀 이름의 우승할 확률을 구할 수 있다.

((L+O) × (L+V) × (L+E) × (O+V) × (O+E) × (V+E)) mod 100

영어 이름과 팀 이름 후보 N개가 주어졌을 때, 우승할 확률이 가장 높은 팀 이름을 구해보자. 확률이 가장 높은 팀이 여러가지인 경우 사전 순으로 가장 앞서는 팀 이름이 우승할 확률이 가장 높은 것이다.

입력
첫째 줄에 영어 이름이 주어진다. 둘째 줄에는 팀 이름 후보의 개수 N이 주어진다. 셋째 줄부터 N개의 줄에 팀 이름이 한 줄에 하나씩 주어진다.

영어 이름과 팀 이름은 길이는 1보다 크거나 같고, 20보다 작거나 같으며, 알파벳 대문자로만 이루어져 있다. N은 50보다 작거나 같은 자연수이다.

출력
첫째 줄에 우승할 확률이 가장 높은 팀 이름을 출력한다.
'''


def getScore(nm, tNm):
  st = nm+tNm
  L = st.count('L')
  O = st.count('O')
  V = st.count('V')
  E = st.count('E')
  val = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100
  return val

name = input()
N = int(input())
teamName = []
for i in range(N):
  teamName.append(input())
teamName.sort()

maxVal = -1
maxIdx = 0
for i in range(N):
  val = getScore(name, teamName[i])
  if val > maxVal:
    maxVal = val
    maxIdx = i
print(teamName[maxIdx])
