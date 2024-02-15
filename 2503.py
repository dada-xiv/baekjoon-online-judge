'''
문제
숫자야구 게임을 하기로 했다.
Y는 1에서 9까지의 서로 다른 숫자 세 개로 구성된 세 자리 수를 마음속으로 생각한다. (예: 324)
M은 1에서 9까지의 서로 다른 숫자 세 개로 구성된 세 자리 수를 Y에게 묻는다. (예: 123)
M이 말한 세 자리 수에 있는 숫자들 중 하나가 Y의 세 자리 수의 동일한 자리에 위치하면 스트라이크 한 번으로 센다. 숫자가 Y의 세 자리 수에 있긴 하나 다른 자리에 위치하면 볼 한 번으로 센다.

예) Y가 324를 갖고 있으면 
429는 1 스트라이크 1 볼이다.
241은 0 스트라이크 2 볼이다.
924는 2 스트라이크 0 볼이다.

Y는 M이 말한 수가 몇 스트라이크 몇 볼인지를 답해준다. M이 Y의 세 자리 수를 정확하게 맞추어 3 스트라이크가 되면 게임이 끝난다. 아니라면 M은 새로운 수를 생각해 다시 Y에게 묻는다. 현재 M이와 Y는 게임을 하고 있는 도중에 있다. M이 Y에게 어떤 수들을 물어보았는지, 그리고 각각의 물음에 Y가 어떤 대답을 했는지가 입력으로 주어진다. 이 입력을 바탕으로 정답으로 가능한 수가 총 몇 개인지를 알아맞혀야 한다.

아래와 같은 경우를 생각해보자.  

M: 123
Y: 1 스트라이크 1 볼.
M: 356
Y: 1 스트라이크 0 볼.
M: 327
Y: 2 스트라이크 0 볼.
M: 489
Y: 0 스트라이크 1 볼.

이때 가능한 답은 324와 328, 이렇게 두 가지이다.
M의 물음들과 각각의 물음에 대한 Y의 답이 입력으로 주어질 때, 정답으로 가능한 수의 개수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에는 M이 Y에게 몇 번이나 질문을 했는지를 나타내는 1 이상 100 이하의 자연수 N이 주어진다. 이어지는 N개의 줄에는 각 줄마다 M이 질문한 세 자리 수와 Y가 답한 스트라이크 개수를 나타내는 정수와 볼의 개수를 나타내는 정수, 이렇게 총 세 개의 정수가 빈칸을 사이에 두고 주어진다.

출력
첫 줄에 Y가 생각하고 있을 가능성이 있는 답의 총 개수를 출력한다.
'''

from itertools import permutations

def getThree(num, s, b):
  nd = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
  numStr = str(num)
  res = set()
  if s == 3:
    res = {num}
  elif s == 2:
    arr = nd-{numStr[0], numStr[1], numStr[2]}
    for el in arr:
      res.add(numStr[0]+numStr[1]+el)
      res.add(numStr[0]+el+numStr[2])
      res.add(el+numStr[1]+numStr[2])
  elif s == 1:
    if b == 0:
      arr = nd-{numStr[0], numStr[1], numStr[2]}
      for li in list(permutations(arr, 2)):
        res.add(numStr[0]+li[0]+li[1])
        res.add(li[0]+numStr[1]+li[1])
        res.add(li[0]+li[1]+numStr[2])
    elif b == 1:
      arr = nd-{numStr[0], numStr[1], numStr[2]}
      for el in arr:
        res.add(numStr[0]+el+numStr[1])
        res.add(numStr[0]+numStr[2]+el)
        res.add(el+numStr[1]+numStr[0])
        res.add(numStr[2]+numStr[1]+el)
        res.add(el+numStr[0]+numStr[2])
        res.add(numStr[1]+el+numStr[2])
    elif b == 2:
      res.add(numStr[0]+numStr[2]+numStr[1])
      res.add(numStr[2]+numStr[1]+numStr[0])
      res.add(numStr[1]+numStr[0]+numStr[2])
  elif s == 0:
    if b == 0:
      arr = nd-{numStr[0], numStr[1], numStr[2]}
      for li in list(permutations(arr, 3)):
        res.add(li[0]+li[1]+li[2])
    elif b == 1:
      arr = nd-{numStr[0], numStr[1], numStr[2]}
      for li in list(permutations(arr, 2)):
        res.add(li[0]+numStr[0]+li[1])
        res.add(li[0]+li[1]+numStr[0])
        res.add(numStr[1]+li[0]+li[1])
        res.add(li[0]+li[1]+numStr[1])
        res.add(numStr[2]+li[0]+li[1])
        res.add(li[0]+numStr[2]+li[1])
    elif b == 2:
      arr = nd-{numStr[0], numStr[1], numStr[2]}
      for el in arr:
        res.add(el+numStr[2]+numStr[1])
        res.add(numStr[2]+el+numStr[1])
        res.add(numStr[1]+numStr[2]+el)
        res.add(el+numStr[2]+numStr[0])
        res.add(numStr[2]+el+numStr[0])
        res.add(numStr[2]+numStr[0]+el)
        res.add(el+numStr[0]+numStr[1])
        res.add(numStr[1]+el+numStr[0])
        res.add(numStr[1]+numStr[0]+el)
    elif b == 3:
      res.add(numStr[2]+numStr[0]+numStr[1])
      res.add(numStr[1]+numStr[2]+numStr[0])
  return res

curSet = set()
n = int(input())
for i in range(n):
  numTry, s, b = map(int, input().split())
  if not curSet:
    curSet = getThree(numTry, s, b)
  else:
    curSet = curSet & getThree(numTry, s, b)

print(len(curSet))
