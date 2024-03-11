M = int(input())
N = int(input())
arr = []

for num in range(M, N+1):
    count = 0
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                count += 1
                break
        if count == 0:
            arr.append(num) 
            
if len(arr) > 0:
    print(sum(arr))
    print(min(arr))
else:
    print(-1)