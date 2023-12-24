T = int(input())

for _ in range(T):
    N = int(input())
    price = list(map(int, input().split()))

    answer = 0
    maxPrice = price[-1]

    for i in range(len(price)-1, -1, -1):
        if price[i] > maxPrice:
            maxPrice = price[i]
        else:
            answer += maxPrice - price[i]

    print(answer)