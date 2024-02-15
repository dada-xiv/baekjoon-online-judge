'''
Problem

The rules of the game are: standing in a circle, the cows sequentially count upward from one, each cow saying a single number when it is her turn. If a cow ever reaches a multiple of 3, however, she should say "Moo" instead of that number. If a cow reaches a multiple of 5, she should say "Moo" instead of that number. If a cow reaches a multiple of 15, she should say "Moo" instead of that number. A transcript of the first part of a game is therefore:

1, 2, Moo, 4, Moo, Moo, 7, 8, Moo, Moo, 11, Moo, 13, 14, Moo, 16

Given N (1 ≤ N 10^9), determine the Nth number spoken in this game.

Input

A single integer, N (1 ≤ N 10^9).

Output

Print out the Nth number spoken during the game.
'''

a = [1, 2, 4, 7, 8, 11, 13, 14]
col = 8
n = int(input())
row = n//col
k = n % col

if k == 0:
  row = row-1
  k = k-1
else:
  k = k-1

print(row*15+a[k])