import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())
nums = deque([])
result = []

for i in range(N):
    nums.append(i+1)   

while nums:
    for i in range(K-1):
        nums.append(nums.popleft())
    result.append(nums.popleft())

print("<", end='')

for i in range(len(result)-1):
    print(result[i], end=', ')

print(result[-1], end='>')