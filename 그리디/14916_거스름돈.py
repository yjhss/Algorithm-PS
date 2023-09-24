import sys
input = sys.stdin.readline
n = int(input())
cnt = 0

if n == 1 or n == 3:
    print(-1)
else:
    while True:
        if n%5 == 0:
            cnt += n//5
            break
        else:
            n -= 2
            cnt += 1
    
        if n <= 0:
            break

    print(cnt)