'''
문제
팰린드롬이란, 앞에서부터 읽었을 때와 뒤에서부터 읽었을 때가 같은 문자열을 말한다. 팰린드롬의 예시로 AAA, ABBA, ABABA 등이 있고, 팰린드롬이 아닌 문자열의 예시로 ABCA, PALINDROME 등이 있다.

어떤 문자열이 팰린드롬인지 판별하는 문제는 재귀 함수를 이용해 쉽게 해결할 수 있다. 아래 코드의 isPalindrome 함수는 주어진 문자열이 팰린드롬이면 1, 팰린드롬이 아니면 0을 반환하는 함수다.

def recursion(s, l, r):
  if l >= r:
    return 1
  elif s[l] != s[r]:
    return 0
  else:
    return recursion(s, l+1, r-1)

def isPalindrome(s):
  return recursion(s, 0, len(s)-1)

위에 작성된 isPalindrome 함수를 이용하여 어떤 문자열이 팰린드롬인지 여부를 판단하려고 한다. 구체적으로는, 문자열 S를 isPalindrome 함수의 인자로 전달하여 팰린드롬 여부를 반환값으로 알아낼 것이다. 더불어 판별하는 과정에서 recursion 함수를 몇 번 호출하는지 셀 것이다. 함수의 반환값과 recursion 함수의 호출 횟수를 구해보자.

입력
첫째 줄에 테스트케이스의 개수 T가 주어진다. (1 ≤ T ≤ 1000)
둘째 줄부터 T개의 줄에 알파벳 대문자로 구성된 문자열 S가 주어진다. (1 ≤ |S| ≤ 1000)

출력
각 테스트케이스마다 isPalindrome 함수의 반환값과 recursion 함수의 호출 횟수를 한 줄에 공백으로 구분하여 출력한다.
'''


def recursion(s, l, r, cnt):
  cnt += 1
  if l >= r:
    return 1, cnt
  elif s[l] != s[r]:
    return 0, cnt
  else:
    return recursion(s, l+1, r-1, cnt)

def isPalindrome(s):
  return recursion(s, 0, len(s)-1, 0)

T = int(input())
for _ in range(T):
  s = input()
  isPalindrome(s)
  print(" ".join(map(str, isPalindrome(s))))
