'''
문제
피보나치 수를 재귀호출과 동적 프로그래밍으로 구할 때, 재귀호출에 비해 동적 프로그래밍이 얼마나 빠른지 확인해 보자. 아래 의사 코드를 이용하여 n의 피보나치 수를 구할 경우 코드1 코드2 실행 횟수를 출력하자.

피보나치 수 재귀호출 의사 코드는 다음과 같다.

fib(n) {
    if (n = 1 or n = 2)
    then return 1;  # 코드1
    else return (fib(n - 1) + fib(n - 2));
}
피보나치 수 동적 프로그래밍 의사 코드는 다음과 같다.

fibonacci(n) {
    f[1] <- f[2] <- 1;
    for i <- 3 to n
        f[i] <- f[i - 1] + f[i - 2];  # 코드2
    return f[n];
}
입력
첫째 줄에 n(5 ≤ n ≤ 40)이 주어진다.

출력
코드1 코드2 실행 횟수를 한 줄에 출력한다.
'''

'''
def fib(n):
  if n == 1 or n == 2:
    return 1  # 코드1
  else:
    return (fib(n - 1) + fib(n - 2))
'''
def fibonacci(n):
  f = [0, 1, 1]
  if n < 3:
    return 1, 1
  else:
    cnt = 0
    for i in range(3, n+1):
      f.append(f[i-1]+f[i-2])  # 코드2
      cnt += 1
    return f[n], cnt

n = int(input())
print(" ".join(map(str, fibonacci(n))))
