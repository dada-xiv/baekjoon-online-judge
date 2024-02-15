'''
문제
찾은 수에 포함된 숫자들을 섞어 30의 배수가 되는 가장 큰 수를 계산하는 프로그램을 작성하라.

입력
N을 입력받는다. N는 최대 10^5개의 숫자로 구성되어 있으며, 0으로 시작하지 않는다.

출력
만들고 싶어하는 수가 존재한다면 그 수를 출력하라. 그 수가 존재하지 않는다면, -1을 출력하라.
'''

nStr = input()
if "0" not in nStr:
  print(-1)
else:
  sum = 0
  for i in range(len(nStr)):
    sum += int(nStr[i])
  if sum % 3 != 0:
    print(-1)
  else:
    nStrSorted = sorted(nStr, reverse=True)
    print("".join(nStrSorted))
