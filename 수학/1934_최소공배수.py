T = int(input())

for i in range(T):  
    a, b = map(int,input().split())
    x, y = a, b

    while y != 0:
        temp = x
        x = y
        y = temp % y

    print(a*b // x)