import sys

n = int(sys.stdin.readline())  
s = [input() for i in range(n)]    

def sum(x):
    r = 0
    for i in x:
        if i.isdigit():     
            r += int (i)
    return r

s.sort(key = lambda x: (len(x), sum(x), x))

for i in s:
    print(i)