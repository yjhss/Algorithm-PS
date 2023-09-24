import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
deque = deque(enumerate(map(int,input().split())))
# enumerate 함수 -> (인덱스,요소) ex) deque = [(0,3), (1,2), (2,1), (3,-3), (4,-1)]

for i in range(N):
    p = deque.popleft()  # p = (0,3)
    print(p[0]+1,end=' ')  # p[0] = 0(인덱스), p[1] = 3(요소)
    if p[1]>0: 
        deque.rotate(-(p[1]-1))
    elif p[1]<0:   
        deque.rotate(-p[1])
