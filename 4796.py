'''
문제
캠핑장은 연속하는 20일 중 10일동안만 사용할 수 있다. 이제 막 28일 휴가를 시작했다. 이번 휴가 기간 동안 캠핑장을 며칠동안 사용할 수 있을까? 조금 더 일반화해서 문제를 풀려고 한다. 

캠핑장을 연속하는 P일 중, L일동안만 사용할 수 있다. 이제 막 V일짜리 휴가를 시작했다. 캠핑장을 최대 며칠동안 사용할 수 있을까? (1 < L < P < V)

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스는 한 줄로 이루어져 있고, L, P, V를 순서대로 포함하고 있다. 모든 입력 정수는 int범위이다. 마지막 줄에는 0이 3개 주어진다.

출력
각 테스트 케이스에 대해서 캠핑장을 최대 며칠동안 사용할 수 있는지 예제 출력처럼 출력한다.
'''

cnt = 1
while True:
  l, p, v = map(int, input().split())
  if l == 0 and p == 0 and v == 0:
    break
  q = v//p
  r = v-p*q
  fullDays = q*l
  if l <= r:
    remainingDays = l
  else:
    remainingDays = r
  print(f"Case {cnt}: {fullDays+remainingDays}")
  cnt += 1
