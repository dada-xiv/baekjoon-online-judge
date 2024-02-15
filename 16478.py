'''
Intersecting chords theorem

입력
첫째 줄에 pab, pbc, pcd의 값이 사이에 공백을 한 개씩 두고 차례대로 주어진다. 주어지는 모든 값들은 10,000 이하의 양의 정수이다.

출력
첫째 줄에 영역 d와 a를 구분하는 선분의 길이를 출력한다. 절대/상대 오차는 10-6 까지 허용한다.
'''

a, b, c = map(int, input().split())
print(a*c/b)
