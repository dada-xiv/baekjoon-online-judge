'''
문제
정수가 주어지면, 그 수의 정수 제곱근을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 n이 주어진다. (0 ≤ n < 2^{63})

출력
첫째 줄에 q^2 ≥ n인 가장 작은 음이 아닌 정수 q를 출력한다.
'''

n = int(input())
start = 0
end = n
while start <= end:
  m = (start+end)//2
  if m**2 < n:
    start = m+1
  else:
    end = m-1
print(start)
