'''
(세 자리 수) × (세 자리 수)

input: 첫째 줄에 (1)의 위치에 들어갈 세 자리 자연수가, 둘째 줄에 (2)의 위치에 들어갈 세자리 자연수가 주어진다.

output: 첫째 줄부터 넷째 줄까지 차례대로 (3), (4), (5), (6)에 들어갈 값을 출력한다.
'''
A = int(input())
B = int(input())

B_digit3 = B//100 
B_digit2 = (B//10)%10 
B_digit1 = B % 10

#(3)
line3 = A * B_digit1

#(4)
line4 = A * B_digit2

#(5)
line5 = A * B_digit3

#(6)
sum = line5*100 + line4*10 + line3

print(line3)
print(line4)
print(line5)
print(sum)