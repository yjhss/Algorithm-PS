import sys
input = sys.stdin.readline
n = int(input())

k = [int(input()) for _ in range(n)]
k.sort()

answers = [k[-i]*i for i in range(1, len(k) + 1)]

print(max(answers))