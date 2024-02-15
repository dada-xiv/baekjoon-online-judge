'''
문제
다음의 점화식에 의해 정의된 수열 t(n)을 생각하자:

t(0)=1
t(n)=t(0)*t(n-1)+t(1)*t(n-2)+...+t(n-1)*t(0)
이 정의에 따르면,

t(1)=t(0)*t(0)=1
t(2)=t(0)*t(1)+t(1)*t(0)=2
t(3)=t(0)*t(2)+t(1)*t(1)+t(2)*t(0)=5
...
주어진 입력 0 ≤ n ≤ 35에 대하여 t(n)을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 n (0 ≤ n ≤ 35)이 주어진다.

출력
첫째 줄에 t(n)을 출력한다.
'''


n = int(input())
t = list()
t.append(1)
for i in range(n):
  val = 0
  for j in range(i+1):
    # print(j, i-j, end=' ')
    val += t[j]*t[i-j]
  t.append(val)
print(t[-1])