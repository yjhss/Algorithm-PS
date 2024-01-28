import sys
import heapq as hq
N = int(sys.stdin.readline())

a = []

for i in range(N):
    num = int(sys.stdin.readline())
    if num > 0:
        hq.heappush(a,num)
        
    elif num == 0:
        if a:
            print(hq.heappop(a))

        else:
            print(0)