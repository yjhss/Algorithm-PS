from itertools import combinations
N = int(input()) 
ingredients = [list(map(int,input().split())) for _ in range(N)]
result = 1e9 
for cmbs in [combinations(ingredients,i) for i in range(1,N+1)]:
    for c in cmbs:
        S,B=1,0       
        for s,b in c: 
            S *= s
            B += b 
        result = min(result, abs(S-B)) 
print(result)