import sys
input = sys.stdin.readline

# DP 풀이
def bridge(N,M):
    dp = [[0]*31 for _ in range (31)]

    for i in range(1,M+1):
        dp[1][i] = i
    
    for j in range(2, N+1):
        for k in range(2,M+1):
            dp[j][k] = dp[j-1][k-1] + dp[j][k-1]

    return dp[N][M]

T = int(input())
for _ in range(T):
    N, M = map(int,input().split())
    print(bridge(N,M))

# 다른 풀이: 그냥 조합(mCr)으로 풀 수도 있다.