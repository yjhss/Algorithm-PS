T = int(input())
for _ in range(T):
    s = input().replace(' ', '')
    count = [0] * 26
    for i in s:
        count[ord(i) - 97] += 1
    if count.count(max(count)) > 1:
        print('?')
    else:
        print(chr(97 + count.index(max(count))))