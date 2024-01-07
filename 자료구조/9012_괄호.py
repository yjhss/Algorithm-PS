import sys

T = int(sys.stdin.readline().strip())
for _ in range(T):
    PS = sys.stdin.readline().strip()
    
    stack = []

    for i in PS:
        if i == '(':
            stack.append(i)
        elif i == ')' and stack:
            stack.pop()
        else:
            print('NO')
            break
    else:
        if stack:
            print('NO')
        else:
            print('YES')